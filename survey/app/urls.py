from django.urls import path
from . import views

urlpatterns = [
    path('api/form/<int:pk>', views.SeeMyForm.as_view()),
]
