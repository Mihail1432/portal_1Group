from django.urls import path
from .views import ProfileView, LogoutView, MyDetailView, RegisterView, LoginView, forum_list, forum_detail, \
    portfolio_list, portfolio_detail, event_list, home

urlpatterns = [
    path('', home, name='home'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('forum/', forum_list, name='forum_list'),
    path('forum/<int:id>/', forum_detail, name='forum_detail'),
    path('portfolio/', portfolio_list, name='portfolio_list'),
    path('portfolio/<int:id>/', portfolio_detail, name='portfolio_detail'),
    path('events/', event_list, name='event_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('mymodel/<int:pk>/', MyDetailView.as_view(), name='mymodel_detail'),
    path('accounts/profile/', ProfileView.as_view(), name='user_profile'),

]
