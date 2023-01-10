
from rest_framework import serializers

from videos.models import Video


class Videoserializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'uploaded_date', 'img',
                  'creator', 'url', 'total_views',
                  'category', 'description',
                  'total_likes', 'duration')
