from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=256)
    multiple = models.BooleanField(default=False)
    type = models.CharField(choices=(('int', 'int'), ('string', 'string'), ("choices", "choices")), max_length=32)
    Necessarily = models.BooleanField(default=True)


class Survey(models.Model):
    questions = models.ManyToManyField(Question)
