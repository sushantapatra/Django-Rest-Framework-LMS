from django.contrib import admin
from django.urls import path

from .views import testView, CategoryListView, CategoryDetailView

# /api/
urlpatterns = [
    path('test/', testView, name="test-api"),
    path('categories/', CategoryListView.as_view(), name="category-listview"),
    path('categories/<str:pk>', CategoryDetailView.as_view(),
         name="category-detailview"),
]
