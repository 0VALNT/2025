import django_filters
from .models import Survey, Question, User, Category
from django.db.models import Q

class SurveyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())
    questions = django_filters.ModelMultipleChoiceFilter(queryset=Question.objects.all())
    past_users = django_filters.ModelMultipleChoiceFilter(queryset=User.objects.all())
    one_attempt = django_filters.BooleanFilter()

    class Meta:
        model = Survey
        fields = ['title', 'category', 'questions', 'past_users', 'one_attempt']