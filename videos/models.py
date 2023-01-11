from django.db import models
from django.contrib.auth.models import User
# from base.models import UtubeUser

import uuid


class Video(models.Model):
    PROGRAMMING = 'PR'
    COMMEDY = 'CM'
    DOCUMENTRY = 'DC'
    FOOTBALL = 'FT'
    MUSIC = 'MC'
    GAMING = 'GM'
    OTHERS = 'OT'

    CATEGORY_CHOICES = [
        (PROGRAMMING, 'Computer Programming'),
        (COMMEDY, 'Commedy'),
        (DOCUMENTRY, 'Documentry'),
        (FOOTBALL, 'Football'),
        (MUSIC, 'Music'),
        (GAMING, 'Gaming'),
        (OTHERS, 'Others')]

    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='photo/%Y/%m/%d/')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.FileField(upload_to='vidoes/%Y/%m/%d/')
    total_views = models.IntegerField(default=0)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    description = models.TextField(
        default='New Video has been added', blank=True)
    total_likes = models.IntegerField(default=0)
    duration = models.DurationField()

    def __str__(self):
        return self.title


class Channel(models.Model):
    name = models.CharField(max_length=300, blank=False)
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    channel_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='New channel created', blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_commented_on = models.ForeignKey('Video', on_delete=models.CASCADE)
    date_of_comment = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=False)

    def __str__(self):
        self.comment_by


class Likes(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    liked_by = models.OneToOneField(User, on_delete=models.CASCADE)
    video_liked = models.OneToOneField('Video', on_delete=models.CASCADE)
    time_liked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.liked_by


class Subscritions(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ManyToManyField('Channel')

    def __str__(self):
        self.subscriber
