# Generated by Django 2.0b1 on 2017-11-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Train', '0004_auto_20171111_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='trees',
            name='Answer11',
            field=models.IntegerField(null=True, verbose_name='Answer11'),
        ),
        migrations.AddField(
            model_name='trees',
            name='Answer12',
            field=models.IntegerField(null=True, verbose_name='Answer12'),
        ),
        migrations.AddField(
            model_name='trees',
            name='Answer13',
            field=models.IntegerField(null=True, verbose_name='Answer13'),
        ),
    ]
