"""
URL configuration for softwareLogin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path ,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('auth/', include('django.contrib.auth.urls')),
    path('',include (("base.urls","base"),"base")),
  path('voice_record/', views.voice_record, name='voice_record'),
    path('record_and_recognize/', views.record_and_recognize, name='record_and_recognize'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # static dosya yolu için ayar