from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='avizier-home'),
    path('about/', views.about, name='avizier-about'),
]