from django.contrib import admin
from .models import Question, Survey, Answer, UserAnswers, UserAnswer, Category, SomeModel, AdminSurveyData, \
    AdminChoseQuestionSurveyData, CountOfAnswers, AdminIntQuestionSurveyData, AdminStrQuestionSurveyData

admin.site.register(Question)


class SurveyAdmin(admin.ModelAdmin):
    fields = ['questions', 'one_attempt', 'category']


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer)
admin.site.register(UserAnswers)
admin.site.register(UserAnswer)
admin.site.register(SomeModel)
admin.site.register(Category)
admin.site.register(AdminChoseQuestionSurveyData)
admin.site.register(AdminSurveyData)
admin.site.register(CountOfAnswers)
admin.site.register(AdminIntQuestionSurveyData)
admin.site.register(AdminStrQuestionSurveyData)
