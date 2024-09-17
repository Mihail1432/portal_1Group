from django.urls import path
from diary import views

urlpatterns = [
    path("<str:username>/<int:year>/<int:month>/", views.DairyView.as_view(), name="student-diary")
]

app_name = "diary"