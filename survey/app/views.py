from django.shortcuts import render
from rest_framework import routers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Survey, Question, Answer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from . import serializers
from django.http import HttpResponse


class SeeMyForm(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'form.html'

    def get(self, request, pk):
        try:
            survey = Survey.objects.get(id=pk)
        except:
            return 0
        if request.user in survey.past_users.all() and survey.one_attempt:
            return HttpResponse('Ты уже прошел эту форму')
        return Response({'survey': survey})

    def post(self, request, pk):
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
