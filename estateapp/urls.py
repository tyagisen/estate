from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.HomeDetailView.as_view(), name='detail'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('login/', views.Login.as_view(), name='login'),
    path('home_feature/', views.AddHomeFeature.as_view(), name='add_home_feature'),
    path('view_feature/', views.ViewHomeFeature.as_view(), name='view_home_feature'),
    path('home_details/', views.AddHomeDetail.as_view(), name='add_home_detail'),
    path('delete-home_feature/<int:id>', views.DeleteHomeFeature, name='delete_home_feature'),

]
