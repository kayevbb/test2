# Generated by Django 2.2.8 on 2019-12-08 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0003_post_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='avatar',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
