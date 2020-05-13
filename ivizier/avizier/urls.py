from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='avizier-home'),
    path('targulitc/', views.targulitc, name='targulitc-about'),
    path('bestem/', views.bestem, name='bestem-about'),
    path('eli-np/', views.eli_np, name='eli-np-about'),
    path('hackitall/', views.hackitall, name='hackitall-about'),
    path('acs/', views.acs, name='acs-about'),
    path('3dupb/', views._3dupb, name='3dupb-about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)