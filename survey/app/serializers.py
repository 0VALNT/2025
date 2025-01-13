from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import UserAnswer, Answer, Question, Survey, UserAnswers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class AnswerSerializer(serializers.Serializer):
    class Meta:
        model = Answer
        fields = ['title', ]


class QuestionSerializer(serializers.Serializer):
    class Meta:
        model = Question
        fields = ['title', 'type', 'necessarily', 'answers']


class SurveySerializer(serializers.Serializer):
    class Meta:
        model = Survey
        fields = ['questions', ]


class UserAnswersSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    survey = serializers.PrimaryKeyRelatedField(queryset=Survey.objects.all())

    class Meta:
        model = UserAnswers
        fields = ['user', 'survey']

    def create(self, validated_data):
        return UserAnswers(**validated_data)


class UserAnswerSerializer(serializers.Serializer):
    user_answers = serializers.PrimaryKeyRelatedField(queryset=UserAnswers.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    answer = serializers.CharField(max_length=256)
    class Meta:
        model = UserAnswer
        fields = ['user_answers', 'question', 'answer']

    def create(self, validated_data):
        return UserAnswer(**validated_data)
