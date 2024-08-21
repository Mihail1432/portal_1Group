from django.urls import path
from .views import ForumThreadListView, ForumThreadCreateView

app_name = 'forum'  # Это регистрирует пространство имен 'forum'

urlpatterns = [
    path('', ForumThreadListView.as_view(), name='thread_list'),
    path('create/', ForumThreadCreateView.as_view(), name='create_thread'),
    # Добавьте другие URL-шаблоны по необходимости
]
