from django.contrib import admin
from .models import *



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['address', 'price']


@admin.register(HomeFeatures)
class HomeFeaturesAdmin(admin.ModelAdmin):
    list_display = ['feature_name']
