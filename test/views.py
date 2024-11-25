from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import redirect

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'test/register.html'
    success_url = '/smart/welcome'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'test/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'test/login.html'
 
class HomeView(TemplateView):
    template_name = 'test/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'test/authorized.html'
    login_url = '/admin'

