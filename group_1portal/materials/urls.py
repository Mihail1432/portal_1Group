from django.urls import path
from materials import views

urlpatterns = [
    path("", views.MaterialsHomeView.as_view(), name="home"),
    path("<int:pk>/", views.MaterialDetailView.as_view(), name="material-detail")
]

app_name = "materials"