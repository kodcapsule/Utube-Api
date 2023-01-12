from django.shortcuts import render
from videos.models import Video
from .serializers import Videoserializer
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


# FUNCTION BASED VIEWS

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def VideosList(request):
    print(request.method)
    if (IsAuthenticated):
        if request.method == 'GET':
            videos = Video.objects.all()
            serializer = Videoserializer(videos, many=True)
            return Response(serializer.data)


def index(request):
    return render(request, 'index.html')


# CLASS BASED VIEWS
class ListVideos(generics.ListCreateAPIView):
    serializer_class = Videoserializer
    queryset = Video.objects.all()
