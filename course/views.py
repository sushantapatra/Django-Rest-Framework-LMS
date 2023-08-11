from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView


# Create your views here.
from course.models import Category, Course, Tag
from course.serializers import CategorySerializer, CourseSerializer, TagSerializer


@api_view(['GET'])
def testView(request):
    response = {
        'message': 'Course API Working',
        'url': request.get_full_path()
    }
    return Response(response)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = CategorySerializer()
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
