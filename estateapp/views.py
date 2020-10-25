from django.shortcuts import render,HttpResponse,  HttpResponse, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView, RedirectView,TemplateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
class HomeListView(ListView):
    model = Home
    context_object_name = 'home'
    template_name = 'estateapp/home.html'


class HomeDetailView(DetailView):
    model = Home
    context_object_name = 'home'

# For the dashboard view
class Dashboard(LoginRequiredMixin,TemplateView):
    # model = Home
    context_object_name= 'dashboard'
    template_name = '../templates/dashboard.html'
    # If the user not login then redirect to down url
    login_url='/login'

# For the Login Authentication
class Login(TemplateView):
    # model = Home
    context_object_name= 'login'
    template_name = '../templates/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, self.template_name)

    def post(self,request,*args,**kwargs):

        u=request.POST.get('username')
        p=request.POST.get('pass')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"Login Credentials doesnt match")
            return redirect('login')


class AddHomeFeature(TemplateView):
    # model = Home
    context_object_name = 'add_home_feature'
    template_name = 'estateapp/add_home_feature.html'