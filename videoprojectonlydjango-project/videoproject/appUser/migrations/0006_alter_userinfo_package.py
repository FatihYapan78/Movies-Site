# Generated by Django 4.2.2 on 2023-06-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0005_packagetype_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='package',
            field=models.CharField(max_length=50, null=True, verbose_name='Paket Tipi'),
        ),
    ]