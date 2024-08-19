from django.shortcuts import render, get_object_or_404
from .models import Forum, ForumPost, Portfolio, Event, User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from .forms import RegistrationForm, LoginForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('profile', username=user.username)
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile', username=user.username)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



# Головна сторінка
def home(request):
    return render(request, 'home.html')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    
    def get_queryset(self):
        return User.objects.filter(username=self.kwargs['username'])
    
    def get(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            return self.handle_no_permission()
        return super().get(request, *args, **kwargs)

# Список форумів
def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum_list.html', {'forums': forums})

# Деталі форуму
def forum_detail(request, id):
    forum = get_object_or_404(Forum, id=id)
    posts = ForumPost.objects.filter(forum=forum)
    return render(request, 'forum_detail.html', {'forum': forum, 'posts': posts})

# Список портфоліо
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio_list.html', {'portfolios': portfolios})

# Деталі портфоліо
def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})

# Список подій
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    
    def get_queryset(self):
        return User.objects.filter(username=self.kwargs['username'])
    
    def get(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            return self.handle_no_permission()
        return super().get(request, *args, **kwargs)

# Logout view using class-based view
class CustomLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home')