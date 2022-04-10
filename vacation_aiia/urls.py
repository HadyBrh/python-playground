"""vacation_aiia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path("signup/", views.SignUp.as_view(), name='signup'),
    path('vacations/', views.IndexView.as_view(), name='index'),
    path('vacations/<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    path('vacations/edit/<int:pk>/', views.edit, name='edit'),
    path('vacations/create/', views.create, name='create'),
    path('vacations/delete/<int:pk>/', views.delete, name='delete'),

]
