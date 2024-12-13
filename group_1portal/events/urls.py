from django.urls import path
from events import views

urlpatterns = [
    path('', views.EventHomeView.as_view(), name='home'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
]

app_name = "events"