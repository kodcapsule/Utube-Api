from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.VideosList, name='index'),
    path('videos/', views.ListVideos.as_view()),
]
