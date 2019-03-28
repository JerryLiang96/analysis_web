"""analysis_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'admin/', admin.site.urls),
    path(r'login/', views.web_login, name='web_login'),
    path(r'logout/', views.web_logout, name='web_logout'),
    path(r'register/', views.web_register, name='web_register'),
    path(r'user_info/', views.user_info, name='user_info'),
    path(r'', include('comment.urls')),
]
