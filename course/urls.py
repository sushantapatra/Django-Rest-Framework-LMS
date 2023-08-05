from django.contrib import admin
from django.urls import path

from .views import testView, CategoryListView

# /api/
urlpatterns = [
    path('test/', testView, name="test-api"),
    path('categories/', CategoryListView.as_view(), name="api-categories"),
]
