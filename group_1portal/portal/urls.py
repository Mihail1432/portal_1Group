from django.contrib import admin
from django.urls import path
from . import views
from .views import UserProfileView, CustomLogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
    path('forum/', views.forum_list, name='forum_list'),
    path('forum/<int:id>/', views.forum_detail, name='forum_detail'),
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    path('events/', views.event_list, name='event_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
