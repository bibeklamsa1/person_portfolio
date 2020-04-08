from django.contrib import admin
from django.urls import path
from .views import blog_called
urlpatterns = [
    path('',blog_called,name="blog"),
]
