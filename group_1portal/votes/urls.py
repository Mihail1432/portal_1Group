from django.urls import path
from votes import views

urlpatterns = [
    path("", views.VoteHomeView.as_view(), name="home"),
    path("search/", views.VoteSearchView.as_view(), name="search"),
    path("<int:pk>/", views.VoteDetailView.as_view(), name="vote-detail"),
    path("<int:pk>/complete", views.VoteCompleteView.as_view(), name="vote-complete")
]

app_name = "votes"