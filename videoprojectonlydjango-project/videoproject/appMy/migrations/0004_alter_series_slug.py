# Generated by Django 4.1.5 on 2023-05-11 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_alter_movie_yil_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug Film'),
        ),
    ]
