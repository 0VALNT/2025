from django.contrib import admin
from .models import Question, Survey, Answer, UserAnswers, UserAnswer, Category

admin.site.register(Question)


class SurveyAdmin(admin.ModelAdmin):
    fields = ['questions', 'one_attempt', 'category']


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer)
admin.site.register(UserAnswers)
admin.site.register(UserAnswer)
admin.site.register(Category)
