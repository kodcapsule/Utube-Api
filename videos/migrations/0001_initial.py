# Generated by Django 4.1.5 on 2023-01-08 13:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('url', models.FileField(upload_to='vidoes/%Y/%m/%d/')),
                ('total_views', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('PR', 'Computer Programming'), ('CM', 'Commedy'), ('DC', 'Documentry'), ('FT', 'Football'), ('MC', 'Music'), ('GM', 'Gaming'), ('OT', 'Others')], max_length=3)),
                ('description', models.TextField(blank=True, default='New Video has been added')),
                ('total_likes', models.IntegerField(default=0)),
                ('duration', models.DurationField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.utubeuser')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField()),
                ('description', models.TextField(blank=True, default='New channel created')),
                ('channel_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.utubeuser')),
            ],
        ),
    ]
