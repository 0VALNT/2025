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
        return Response({'survey': survey})

    def post(self, request, pk):
        try:
            survey = Survey.objects.get(id=pk)
        except:
            return 0
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

        return HttpResponse('ads')
