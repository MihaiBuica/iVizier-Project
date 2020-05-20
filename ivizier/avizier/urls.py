from django.urls import path

from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='avizier-home'),
    # path('add-post/', views.PostCreateView.as_view(template_name='add-post.html'), name='add-post'),
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