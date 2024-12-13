from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from portfolio.mixins import UserIsOwner
from portfolio.models import PortfolioItem
from portfolio.forms import PortfolioItemForm


class PortfolioHomeView(ListView):
    model = PortfolioItem
    context_object_name = "portfolios"
    template_name = "portfolio/home.html"


class PortfolioCreateView(CreateView):
    model = PortfolioItem
    form_class = PortfolioItemForm
    template_name = "portfolio/portfolio_create.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        self.object = form.instance

        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy("portfolio:portfolio-detail", kwargs={"pk": self.object.pk})


class PortfolioDetailView(DetailView):
    model = PortfolioItem
    context_object_name = "portfolio"
    template_name = "portfolio/portfolio_detail.html"


class PortfolioUpdateView(UserIsOwner, UpdateView):
    model = PortfolioItem
    form_class = PortfolioItemForm
    context_object_name = "portfolio"
    template_name = "portfolio/portfolio_update.html"

    def get_success_url(self) -> str:
        return reverse_lazy("portfolio:portfolio-detail", kwargs={"pk": self.object.pk})


class PortfolioDeleteView(UserIsOwner, DeleteView):
    model = PortfolioItem
    success_url = reverse_lazy("portfolio:home")