from django.shortcuts import render
from videos.models import Video
from .serializers import Videoserializer

from rest_framework import generics
# Create your views here.


def index(request):
    return render(request, 'index.html')


class ListVideos(generics.ListCreateAPIView):
    serializer_class = Videoserializer
    queryset = Video.objects.all()
   
