import math
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView
from django.urls import reverse_lazy
from core.mixins import UserIsStaffMixin, UserHasNotCompletedMixin
from surveys.models import Survey, Question, Option

# Create your views here.
class SurveyHomeView(TemplateView):
    template_name = "surveys/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["recent"] = Survey.objects.all()[:10]

        return context


class SurveySearchView(ListView):
    model = Survey
    context_object_name = "surveys"
    template_name = "surveys/survey_search.html"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("query")

        matched_queryset = queryset.filter(Q(title__contains=search_query) | Q(description__contains=search_query))

        return matched_queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["results_amount"] = len(self.get_queryset())

        return context
    

class SurveyDetailView(DetailView):
    model = Survey
    template_name = "surveys/survey_detail.html"
    context_object_name = "survey"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = self.get_object().questions.all()

        context["slides"] = range(0, math.ceil(len(questions) / 3)*3, 3)

        return context


class SurveyCompleteView(UserHasNotCompletedMixin, DetailView):
    model = Survey
    template_name = "surveys/survey_complete.html"
    context_object_name = "survey"

    def post(self, request, *args, **kwargs):
        survey = self.get_object()
        survey.save_submition(request)

        return redirect("surveys:survey-detail", pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = self.get_object().questions.all()

        context["slides"] = range(0, math.ceil(len(questions) / 3)*3, 3)

        return context
    

class SurveyResultsView(UserIsStaffMixin, DetailView):
    model = Survey
    template_name = "surveys/survey_results.html"
    context_object_name = "survey"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = self.get_object().questions.all()

        context["slides"] = range(0, math.ceil(len(questions) / 3)*3, 3)

        return context