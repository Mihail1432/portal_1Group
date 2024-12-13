from django.urls import path
from surveys import views

urlpatterns = [
    path("", views.SurveyHomeView.as_view(), name="home"),
    path("search/", views.SurveySearchView.as_view(), name="search"),
    path("<int:pk>/", views.SurveyDetailView.as_view(), name="survey-detail"),
    path("<int:pk>/complete/", views.SurveyCompleteView.as_view(), name="survey-complete"),
    path("<int:pk>/results/", views.SurveyResultsView.as_view(), name="survey-results")
]

app_name = "surveys"