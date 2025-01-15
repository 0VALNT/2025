from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Survey, Answer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from . import serializers
from django.http import HttpResponse


class ProtectedViews(APIView):

    def get(self, request, token=None):
        if token:
            try:
                validated_token = JWTAuthentication().get_validated_token(token)
                print('asd')
                user = JWTAuthentication().get_user(validated_token)
                request.user = user
            except Exception as e:
                raise AuthenticationFailed('Invalid token')

        return Response({"message": "This is a protected view!", "user": str(request.user)})


class SeeMyForm(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'form.html'

    def get(self, request, pk, token=None):
        if token:
            try:
                validated_token = JWTAuthentication().get_validated_token(token)
                print('asd')
                user = JWTAuthentication().get_user(validated_token)
                request.user = user
            except Exception as e:
                raise AuthenticationFailed('Invalid token')
        try:
            survey = Survey.objects.get(id=pk)
        except:
            return 0
        if request.user in survey.past_users.all() and survey.one_attempt:
            return HttpResponse('Ты уже прошел эту форму')
        return Response({'survey': survey})

    def post(self, request, pk, token):
        if token:
            try:
                validated_token = JWTAuthentication().get_validated_token(token)
                print('asd')
                user = JWTAuthentication().get_user(validated_token)
                request.user = user
            except Exception as e:
                raise AuthenticationFailed('Invalid token')
        try:
            survey = Survey.objects.get(id=pk)
        except:

            return 0
        if request.user in survey.past_users.all() and survey.one_attempt:
            return HttpResponse('Ты уже прошел эту форму')
        user = request.user
        serializer = serializers.UserAnswersSerializer(data={
            'user': user.id,
            'survey': survey.id,
        })
        if serializer.is_valid():
            print('True')
            obj = serializer.save()
            obj.save()
        else:
            return 0
        post = request.POST
        for question in survey.questions.all():
            if question.type == 'choices':
                answer = Answer.objects.get(id=int(request.POST[f'{question.id}'])).title
            elif question.type == 'multiple_choice':
                answers = post.getlist(f'{question.id}')
                print(answers)
                answer = ''
                for i in answers:
                    print(i)
                    answer += Answer.objects.get(id=int(i)).title + ' '
                print(answer)
            else:
                answer = request.POST[f'{question.id}']
            serializer = serializers.UserAnswerSerializer(data={
                'answer': answer,
                'question': question.id,
                'user_answers': obj.id
            })
            if serializer.is_valid():
                print('True')
                objec = serializer.save()
                objec.save()
        survey.past_users.add(user)
        return HttpResponse('ads')
