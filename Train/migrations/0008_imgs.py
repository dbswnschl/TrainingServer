# Generated by Django 2.0b1 on 2017-11-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Train', '0007_auto_20171114_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImgNum', models.IntegerField(verbose_name='ImgNum')),
                ('ImgData', models.TextField(max_length=31340, verbose_name='ImgData')),
            ],
        ),
    ]