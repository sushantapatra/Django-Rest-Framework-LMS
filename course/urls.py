from django.contrib import admin
from django.urls import path, include

from .views import CategorySlugDetailView, testView, CategoryViewSet, CourseViewSet, TagViewSet, CourseSlugDetailView
from rest_framework.routers import DefaultRouter

# /api/
category_router = DefaultRouter()
category_router.register('', CategoryViewSet, basename="category")
# category-list
# category-detail

course_router = DefaultRouter()
course_router.register('', CourseViewSet, basename="course")
# course-list
# course-detail

tag_router = DefaultRouter()
tag_router.register('', TagViewSet, basename="tag")
# tag-list
# tag-detail

# print(router.urls)
urlpatterns = [
    path('test/', testView, name="test-api"),
    path('category/slug/<str:slug>', CategorySlugDetailView.as_view(),
         name="category-detail-by-slug"),
    path('category/', include(category_router.urls)),
    path('tag/', include(tag_router.urls)),
    path('', include(course_router.urls)),
    path('slug/<str:slug>', CourseSlugDetailView.as_view(),
         name="course-detail-by-slug"),
]
