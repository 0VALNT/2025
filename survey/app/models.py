from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Answer(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=256)
    type = models.CharField(
        choices=(('int', 'int'), ('string', 'string'), ("choices", "choices"), ('multiple_choice', 'multiple_choice')),
        max_length=32)
    necessarily = models.BooleanField(default=True)
    answers = models.ManyToManyField(Answer, null=True, default='-')


class Survey(models.Model):
    questions = models.ManyToManyField(Question)
    past_users = models.ManyToManyField(User)
    one_attempt = models.BooleanField(default=True)

class UserAnswer(models.Model):
    user_answers = models.ForeignKey('UserAnswers', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)


class UserAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE)
