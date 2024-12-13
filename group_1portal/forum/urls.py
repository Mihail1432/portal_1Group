from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('<int:forum_id>/', views.forum_detail, name='forum_detail'),
    path('create/', views.create_forum, name='create_forum'),
    path('forum/<int:forum_id>/edit/', views.edit_forum, name='edit_forum'),
    path('forum/<int:forum_id>/delete/', views.delete_forum, name='delete_forum'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]


