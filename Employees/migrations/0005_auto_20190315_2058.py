# Generated by Django 2.1.7 on 2019-03-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0004_auto_20190315_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Изображение'),
        ),
    ]
