# Generated by Django 4.1.5 on 2023-06-04 21:38

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0016_remove_movie_video_movie_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='url',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
