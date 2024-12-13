from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from announcements.models import Announcement
from diary.models import Grade
from events.models import Event
import datetime

# Create your views here.
class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["announcements"] = Announcement.objects.all()[:3]

        context["events"] = Event.objects.all()[:3]

        now = datetime.date.today()
        context["grades"] = Grade.objects.filter(date__year=now.year, date__month=now.month)
        context["total"] = sum(grade.logiks for grade in context["grades"])
        
        return context