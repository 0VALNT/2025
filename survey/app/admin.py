from django.contrib import admin
from .models import Question, Survey, Answer, UserAnswers, UserAnswer

admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(Answer)
admin.site.register(UserAnswers)
admin.site.register(UserAnswer)

