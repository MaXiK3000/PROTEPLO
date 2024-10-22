"""
URL configuration for proteplo project.

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
from django.urls import path, re_path, include
from proteplo_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('services/<slug:slug>', views.service),
    path('services', views.services),
    path('informations/<slug:slug>', views.information),
    path('informations', views.informations),
    path('gallery/<slug:slug>', views.gallery),
    path('gallery', views.gallerys),
    path('about_us', views.aboutUs),
    path('contacts', views.contacts),
    path('reviews', views.reviews),
    path('', views.main),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
