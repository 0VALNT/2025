from django.shortcuts import redirect
from rest_framework import status, generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django_filters import rest_framework as filters

from .filters import SurveyFilter
from .models import Survey, Answer, SomeModel
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from . import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


def login(request):
    token = request.COOKIES['access']
    if token:
        try:
            validated_token = JWTAuthentication().get_validated_token(token)
            user = JWTAuthentication().get_user(validated_token)
            request.user = user
        except Exception as e:
            res = [True, request]
            return res
        res = [False, request]
        return res
    else:
        res = [True, request]
        return res


class Login(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        print(serializer.validated_data['access'])
        response.set_cookie('access', value=serializer.validated_data['access'])
        return response


class ProtectedViews(APIView):

    def get(self, request, token=None):
        if token:
            try:
                validated_token = JWTAuthentication().get_validated_token(token)
                user = JWTAuthentication().get_user(validated_token)
                request.user = user
            except Exception as e:
                raise AuthenticationFailed('Invalid token')

        return Response({"message": "This is a protected view!", "user": str(request.user)})


class SeeMyForm(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'form.html'

    def get(self, request, pk):
        log = login(request)
        if log[0]:
            return redirect('token_obtain_pair')
        else:
            request = log[1]
        try:
            survey = Survey.objects.get(id=pk)
        except:
            return 0
        if request.user in survey.past_users.all() and survey.one_attempt:
            return HttpResponse('Ты уже прошел эту форму')
        return Response({'survey': survey})

    def post(self, request, pk):
        log = login(request)
        if log[0]:
            return redirect('token_obtain_pair')
        else:
            request = log[1]
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
                answer = ''
                for i in answers:
                    answer += Answer.objects.get(id=int(i)).title + ' '
            else:
                answer = request.POST[f'{question.id}']
            serializer = serializers.UserAnswerSerializer(data={
                'answer': answer,
                'question': question.id,
                'user_answers': obj.id
            })
            if serializer.is_valid():
                objec = serializer.save()
                objec.save()
        survey.past_users.add(user)
        return HttpResponse('ads')


class Profile(APIView):
    def get(self, request):
        log = login(request)
        if log[0]:
            return redirect('token_obtain_pair')
        else:
            request = log[1]
        serializer = serializers.UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

    def put(self, request, token):
        log = login(request)
        if log[0]:
            return redirect('token_obtain_pair')
        else:
            request = log[1]
        serializer = serializers.UserSerializer(data=request.data, instance=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


class SomeView(APIView):
    def get(self, request, pk):
        some = SomeModel.objects.get(id=pk)
        serializer = serializers.SomeModelSerializer(some)
        return Response(serializer.data)

    def put(self, request, pk):
        some = SomeModel.objects.get(id=pk)
        serializer = serializers.SomeModelSerializer(data=request.data, instance=some)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


class SomeList(ListCreateAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = serializers.SomeModelSerializer
    filter_fields = (
        'email',
        'username',
    )


class ChangePasswordView(UpdateAPIView):
    serializer_class = serializers.ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        log = login(self.request)
        if log[0]:
            return redirect('token_obtain_pair')
        else:
            request = log[1]
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = serializers.SurveySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SurveyFilter
