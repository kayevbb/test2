# Generated by Django 2.2.8 on 2019-12-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0004_auto_20191208_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='bektur',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fields',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fields',
            name='photo',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fields',
            name='avatar',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
    ]
