"""wr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from api.views import GetTokenView, ValidateTokenView
from api.admin_views import UserManagementView

urlpatterns = [
    path("User/GetToken", GetTokenView.as_view()),
    path("User/ValidateToken", ValidateTokenView.as_view()),
    path("Admin/UserManagement", UserManagementView.as_view()),
    path("Admin/UserManagement/<int:user_id>", UserManagementView.as_view()),
]
