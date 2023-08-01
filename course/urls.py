from django.contrib import admin
from django.urls import path

from .views import testView

# /api/course/
urlpatterns = [
    path('test/', testView, name="test-api")
]
