# Generated by Django 4.2.2 on 2023-06-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0026_delete_bildirim'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanlıVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Kanal Adı')),
                ('image', models.ImageField(upload_to='CanlıYayın', verbose_name='Kanal Resmi')),
                ('url', models.CharField(max_length=50, verbose_name='Url')),
            ],
        ),
    ]
