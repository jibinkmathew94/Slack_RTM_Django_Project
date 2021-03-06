# Generated by Django 2.1.5 on 2019-01-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_upvote', '0002_remove_youtubevideo_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtubevideo',
            old_name='link',
            new_name='video_id',
        ),
        migrations.AddField(
            model_name='youtubevideo',
            name='thumbnail_url',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='youtubevideo',
            name='title',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
