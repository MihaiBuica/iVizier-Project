from django.urls import path

from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='avizier-home'),
    path('an1/', views.an1, name="an1"),
    path('an2/', views.an2, name="an2"),
    path('an3/', views.an3, name="an3"),
    path('an4/', views.an4, name="an4"),
    path('anpub/', views.anpub, name="anpub"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('add-post/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('targulitc/', views.targulitc, name='targulitc-about'),
    # path('bestem/', views.bestem, name='bestem-about'),
    # path('eli-np/', views.eli_np, name='eli-np-about'),
    # path('hackitall/', views.hackitall, name='hackitall-about'),
    # path('acs/', views.acs, name='acs-about'),
    # path('3dupb/', views._3dupb, name='3dupb-about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)