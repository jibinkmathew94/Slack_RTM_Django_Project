# Generated by Django 2.1.5 on 2019-01-17 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_upvote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubevideo',
            name='author',
        ),
    ]
