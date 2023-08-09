"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from root.views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name="api_root"),
    path('api/', api_root, name="api_root"),
    path('api/course/', include(('course.urls','course'), namespace="course")),
    path('api/chapter/', include(('chapter.urls', 'chapter'),  namespace="chapter")),
    path('api/coupon/', include(('coupon.urls','coupon'), namespace="coupon")),
    path('api/doubt/', include(('doubt.urls', 'doubt'), namespace="doubt")),
    path('api/order/', include(('order.urls', 'order'), namespace='order')),
    path('api/review/', include(('review.urls', 'review'), namespace='review')),
]
