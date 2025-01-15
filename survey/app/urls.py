from django.urls import path
from . import views

urlpatterns = [
    path('api/form/<int:pk>/<str:token>', views.SeeMyForm.as_view()),
    path('api/tests/<str:token>', views.ProtectedViews.as_view()),
]
