from .models import Category, Course, Tag
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
