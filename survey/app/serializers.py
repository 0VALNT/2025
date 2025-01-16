from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import UserAnswer, Answer, Question, Survey, UserAnswers, SomeModel, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance


class AnswerSerializer(serializers.Serializer):
    class Meta:
        model = Answer
        fields = ['title', ]


class QuestionSerializer(serializers.Serializer):
    class Meta:
        model = Question
        fields = ['title', 'type', 'necessarily', 'answers']


class SurveySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    class Meta:
        model = Survey
        fields = '__all__'


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


class SomeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = ['username', 'email']

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
