from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view


# Create your views here.
from course.models import Category
from course.serializers import CategorySerializer


@api_view(['GET'])
def testView(request):
    response = {
        'message': 'Course API Working',
        'url': request.get_full_path()
    }
    return Response(response)


class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
