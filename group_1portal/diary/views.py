from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, MonthArchiveView
from django.contrib.auth import get_user_model
from diary.models import Grade
from datetime import date

# Create your views here.
class DairyView(MonthArchiveView):
    model = Grade
    date_field = "date"
    month_format = "%m"
    allow_empty = True
    context_object_name = "grades"
    template_name = "diary/diary.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        dairy_month = request.POST.get("dairy-month")
        year, month = dairy_month.split("-")

        return redirect(reverse_lazy("diary:student-diary", kwargs={"username": username, "year": year, "month": month}))
        # return redirect("home")

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.kwargs.get("username")
        student = get_user_model().objects.get(username=username)

        queryset = queryset.filter(student=student).order_by("date")
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get("username")

        context["student"] = get_user_model().objects.get(username=username)
        context["total"] = sum(grade.logiks for grade in self.object_list.all())

        return context