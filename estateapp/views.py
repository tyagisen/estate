from django.shortcuts import render,HttpResponse,  HttpResponse, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView, RedirectView,TemplateView


class HomeListView(ListView):
    model = Home
    context_object_name = 'home'
    template_name = 'estateapp/home.html'


class HomeDetailView(DetailView):
    model = Home
    context_object_name = 'home'

class Dashboard(TemplateView):
    # model = Home
    context_object_name= 'dashboard'
    template_name = 'estateapp/dashboard.html'

