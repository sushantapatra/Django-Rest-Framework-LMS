from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from root.permissions import isAdminUserOrReadonly
from rest_framework.response import Response

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
    permission_classes = [isAdminUserOrReadonly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminUserOrReadonly]
    lookup_field = 'slug'
    serializer_class = CategorySerializer()
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    permission_classes = [isAdminUserOrReadonly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    # override the create method for save category instance on course create time
    def create(self, request, *args, **kwargs):
        # return Response("Create Method Called...")
        course = request.data
        category_id = course.get('course_id')

        category = None
        if category_id is None:
            return Response({'category_id': ["category_id is required."]})

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist or ValidationError:
            return Response({'category_id': ["category_id is not valid."]})

        serializer = CourseSerializer(data=course)
        if (serializer.is_valid()):
            courseInstance = Course(
                **serializer.validated_data, category=category)
            courseInstance = courseInstance.save()
            return Response(CategorySerializer(courseInstance).data)

        return Response(serializer.errors)


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [isAdminUserOrReadonly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
