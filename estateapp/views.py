from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class HomeListView(ListView):
    model = Home
    context_object_name = 'home'
    template_name = 'estateapp/home.html'


class HomeDetailView(DetailView):
    model = Home
    context_object_name = 'home'
