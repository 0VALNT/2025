from django.urls import path

from . import views

urlpatterns = [
    path('api/form/<int:pk>/', views.SeeMyForm.as_view()),
    path('api/tests/', views.ProtectedViews.as_view()),
    path('api/user/', views.Profile.as_view()),
    path('api/some-url/<int:pk>', views.SomeView.as_view()),
    path('api/survey-list/', views.SurveyViewSet.as_view({'get': 'list'})),
    path('api/token/', views.Login.as_view(), name='token_obtain_pair'),
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change_password')
]
