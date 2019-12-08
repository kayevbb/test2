# Generated by Django 2.2.8 on 2019-12-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0007_delete_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.CharField(choices=[['male', 'Крытай'], ['female', 'Не крытый']], default='male', max_length=10, verbose_name='Полe'),
        ),
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='номер'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание поля'),
        ),
    ]
