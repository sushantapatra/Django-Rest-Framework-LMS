from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# Create your views here.


@api_view(['GET'])
def api_root(request):
    response = {
        "API Root": reverse('api_root', request=request),
        "Course": {
            "API Course List": reverse('course:course-list', request=request),
            "API Course Details": reverse('course:course-detail', args=[1], request=request),
            "API Course Details By Slug": reverse('course:course-detail-by-slug', args=['laravel-beginner-course'], request=request),
        },
        "Tags": {
            "API Tag List": reverse('course:tag-list', request=request),
            "API Tag Details": reverse('course:tag-detail', args=[2], request=request),
        },
        "Category": {
            "API Category List": reverse('course:category-list', request=request),
            "API Category Details": reverse('course:category-detail', args=['laravel-beginner-course'], request=request),
            "API Category Details By Slug": reverse('course:category-detail-by-slug', args=['test-two'], request=request),
        },





        "API Chapter Test": reverse('chapter:test-api', request=request),
        "API Coupon Test": reverse('coupon:test-api', request=request),
    }
    return Response(response)
