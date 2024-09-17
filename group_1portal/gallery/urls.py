from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.GalleryHomeView.as_view(), name='home'),
    path('image/<int:pk>/', views.ImageDetailView.as_view(), name='image-detail'),
]

app_name = "gallery"