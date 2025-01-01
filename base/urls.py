
from django.urls import path ,include
from .views import authView ,home , logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("", home, name="home"),
    path("signup/" ,authView ,name ="authView"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
   path('search_and_play_turkish/', views.search_and_play_turkish, name='search_and_play_turkish'),
   path('search_and_play_english/', views.search_and_play_english, name='search_and_play_english'),# Buradaki "name" önemli
    path('play-audio/', views.play_audio, name='play_audio'),
   
]

    
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)