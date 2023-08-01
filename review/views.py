from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def testView(request):
    response = {
        "message": "Review Test API Working",
        "url": request.get_full_path(),
    }
    return Response(response)
