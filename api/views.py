from django.shortcuts import render
from videos.models import Video
from .serializers import Videoserializer

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


# FUNCTION BASED VIEWS

@api_view(['GET'])
def VideosList(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


def index(request):
    return render(request, 'index.html')


# CLASS BASED VIEWS
class ListVideos(generics.ListCreateAPIView):
    serializer_class = Videoserializer
    queryset = Video.objects.all()
