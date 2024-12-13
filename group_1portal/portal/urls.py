from django.contrib import admin
from django.urls import path
from . import views
from .views import ProfileView, LogoutView, MyDetailView, RegisterView, LoginView, change_user_permissions


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    path('events/', views.event_list, name='event_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('mymodel/<int:pk>/', MyDetailView.as_view(), name='mymodel_detail'),
    path('change_user_permissions/<str:username>/', change_user_permissions, name='change_user_permissions'),
]
