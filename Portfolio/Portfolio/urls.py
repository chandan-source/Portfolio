"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from My_Portfolio.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('work/<str:type>/', my_work, name='work'),
    path('about', aboutus, name='about'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('work_detail/<int:wid>/', work_detail, name='work_detail'),
    path('blog_detail/<int:bid>/', blog_detail, name='blog_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
