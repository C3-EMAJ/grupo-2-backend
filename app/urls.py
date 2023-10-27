"""app URL Configuration

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
from backendEMAJ import views
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', csrf_exempt(views.user)),
    #path('user/', csrf_exempt(views.createUser)),
    path('assistido/', csrf_exempt(views.createAssistido)),
    path('deleteAssistido/', csrf_exempt(views.deleteAssistido)),
    path('deleteUser/', csrf_exempt(views.deleteUser)),
    path('editAssistido/', csrf_exempt(views.editAssistido))
]
