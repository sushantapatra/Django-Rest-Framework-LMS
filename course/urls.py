from django.contrib import admin
from django.urls import path,include

from .views import testView, CategoryViewSet,CourseViewSet,TagViewSet
from rest_framework.routers import DefaultRouter

# /api/
category_router =DefaultRouter()
category_router.register('',CategoryViewSet, basename="category")

course_router =DefaultRouter()
course_router.register('',CourseViewSet, basename="course")

tag_router =DefaultRouter()
tag_router.register('',TagViewSet, basename="tag")

#print(router.urls)
urlpatterns = [
    path('test/', testView, name="test-api"),
    path('category/', include(category_router.urls)),
    path('course/', include(course_router.urls)),
    path('tag/', include(tag_router.urls)),
]
