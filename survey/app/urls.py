from django.urls import path, include

from . import views

urlpatterns = [
    path('form/<int:pk>/', views.SeeMyForm.as_view()),
    path('tests/', views.ProtectedViews.as_view()),
    path('user/', views.Profile.as_view()),
    path('some-url/<int:pk>', views.SomeView.as_view()),
    path('survey-list/', views.SurveyViewSet.as_view({'get': 'list'})),
    path('token/', views.Login.as_view(), name='token_obtain_pair'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('download_excel/', views.GenerateExcelView.as_view(), name='download_excel'),
    path('download_csv/', views.GenerateCsvView.as_view(), name='download_csv'),
    path('download_excel_user_answers/', views.GenerateExcelUserAnswersView.as_view(),
         name='download_excel_user_answers'),
    path('download_csv_user_answers/', views.GenerateCsvUserAnswersView.as_view(), name='download_csv_user_answers'),
]
