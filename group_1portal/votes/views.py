from typing import Any
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView
from core.mixins import UserHasNotCompletedMixin
from votes.models import Vote

# Create your views here.
class VoteHomeView(TemplateView):
    template_name = "votes/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["recent"] = Vote.objects.all()[:10]

        return context
    
    def post(self, request):
        print(request.POST)

        return self.get(request)
    

class VoteSearchView(ListView):
    model = Vote
    context_object_name = "votes"
    template_name = "votes/vote_search.html"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("query")
        
        matched_queryset = queryset.filter(Q(question__contains=search_query) | Q(description__contains=search_query) | Q(title__contains=search_query))

        return matched_queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["results_amount"] = len(self.get_queryset())

        return context


class VoteDetailView(DetailView):
    model = Vote
    template_name = "votes/vote_detail.html"
    context_object_name = "vote"


class VoteCompleteView(UserHasNotCompletedMixin, DetailView):
    model = Vote
    template_name = "votes/vote_complete.html"
    context_object_name = "vote"

    def post(self, request, *args, **kwargs):
        vote = self.get_object()

        vote.save_submission(request)          

        return redirect("votes:vote-detail", pk=vote.pk)