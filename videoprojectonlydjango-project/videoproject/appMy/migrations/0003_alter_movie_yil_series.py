# Generated by Django 4.1.5 on 2023-05-10 23:32

import appMy.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCategory', '0003_alter_subcategory_slug'),
        ('appMy', '0002_movie_cast_movie_category_movie_director_movie_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='yil',
            field=models.PositiveIntegerField(default=2023, validators=[django.core.validators.MinValueValidator(1984), appMy.models.max_value_current_year]),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Dizi Adı')),
                ('text', models.TextField(max_length=500, verbose_name='Dizi Açıklama')),
                ('image', models.ImageField(upload_to=None, verbose_name='Dizi Resim')),
                ('seasons', models.IntegerField(default=1, verbose_name='Sezon Sayısı')),
                ('episodes', models.IntegerField(default=1, verbose_name='Bölüm Sayısı')),
                ('year', models.PositiveIntegerField(default=2023, validators=[django.core.validators.MinValueValidator(1984), appMy.models.max_value_current_year])),
                ('cast', models.TextField(max_length=500, verbose_name='Oyuncular')),
                ('director', models.CharField(max_length=50, verbose_name='Yönetmen')),
                ('writers', models.CharField(max_length=50, verbose_name='Senarist')),
                ('slug', models.SlugField(verbose_name='Slug Film')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCategory.category', verbose_name='Category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCategory.subcategory', verbose_name='Alt Category')),
            ],
        ),
    ]
