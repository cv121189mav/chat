from django.contrib import admin
from django.urls import path
from ChatApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('chat/', views.chat, name='chat'),
]