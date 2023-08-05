from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.parsers import JSONParser

# Create your views here.
from rest_framework.views import APIView
from course.models import Category
from course.serializers import CategorySerializer


@api_view(['GET'])
def testView(request):
    response = {
        'message': 'Course API Working',
        'url': request.get_full_path()
    }
    return Response(response)


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer_response = CategorySerializer(categories, many=True)
        return Response(serializer_response.data)

    def post(self, request):
        jsonCatdata = JSONParser().parse(request)
        serializer = CategorySerializer(data=jsonCatdata)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


