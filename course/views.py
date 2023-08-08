from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet




# Create your views here.
from course.models import Category,Course,Tag
from course.serializers import CategorySerializer,CourseSerializer,TagSerializer


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

class CourseViewSet(ModelViewSet):
    serializer_class =CourseSerializer
    queryset=Course.objects.all()


class TagViewSet(ModelViewSet):
    serializer_class =TagSerializer
    queryset=Tag.objects.all()
