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
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import MyModel, UserProfile
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy
from django.http import Http404



class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # Перенаправлення на сторінку логіну після успішної реєстрації

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class LoginView(DjangoLoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')



# Головна сторінка
def home(request):
    return render(request, 'home.html')


class ProfileView(DetailView):
    model = User
    template_name = 'profile1.html'
    context_object_name = 'user'
    
    def get_object(self, queryset=None):
        username = self.kwargs.get('username')

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




class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')



class MyDetailView(PermissionRequiredMixin, DetailView):
    model = MyModel
    permission_required = 'app.can_view_mymodel'
    template_name = 'mytemplate.html'

    def handle_no_permission(self):
        return redirect('login')  # Або перенаправлення на іншу сторінку
    

