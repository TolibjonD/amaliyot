from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from django.contrib import messages

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "users/register.html", {"form":form})
    
    def post(self, request):
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered !..")
            return redirect('users:login')
        return render(request, "users/register.html", {"form":form})
    
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "users/login.html", {'form':form})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.info(request, "You have successfully logged in !..")
            return redirect('landing_page')
        return render(request, "users/login.html", {'form':form})
    
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = get_user(self.request)
        form = ProfileUpdateForm(instance=user)
        return render(request, "users/profile.html", {'user':user, "form":form})    
    def post(self, request):
        user = get_user(self.request)
        form = ProfileUpdateForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        return render(request, "users/profile.html", {"user":user, "form":form})    


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out !..")
        return redirect('landing_page')