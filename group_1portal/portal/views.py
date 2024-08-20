from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.views.generic import DetailView, View, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Forum, ForumPost, Portfolio, Event, User, UserProfile, MyModel
from django.contrib.auth.forms import UserCreationForm  # Імпорт UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView  # Імпорт DjangoLoginView


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'portal/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class LoginView(DjangoLoginView):
    template_name = 'portal/login.html'
    success_url = reverse_lazy('home')


def home(request):
    return render(request, 'portal/home.html')


class ProfileView(DetailView):
    model = User
    template_name = 'portal/profile1.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)


def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'portal/forum_list.html', {'forums': forums})


def forum_detail(request, id):
    forum = get_object_or_404(Forum, id=id)
    posts = ForumPost.objects.filter(forum=forum)
    return render(request, 'portal/forum_detail.html', {'forum': forum, 'posts': posts})


def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portal/portfolio_list.html', {'portfolios': portfolios})


def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'portal/portfolio_detail.html', {'portfolio': portfolio})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'portal/event_list.html', {'events': events})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class MyDetailView(PermissionRequiredMixin, DetailView):
    model = MyModel
    permission_required = 'app.can_view_mymodel'
    template_name = 'portal/mytemplate.html'

    def handle_no_permission(self):
        return redirect('login')
