# Generated by Django 4.1.5 on 2023-06-02 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0015_movie_fragman_series_fragman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video',
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.moviesvideo', verbose_name='Film'),
        ),
    ]