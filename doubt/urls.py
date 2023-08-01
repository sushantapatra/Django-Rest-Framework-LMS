from django.contrib import admin
from django.urls import path
from .views import testView
urlpatterns = [
    path('test/', testView, name="api-test")
]
