# Generated by Django 2.0b1 on 2017-11-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Train', '0003_auto_20171111_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='trees',
            name='Answer10',
            field=models.IntegerField(null=True, verbose_name='Answer10'),
        ),
        migrations.AddField(
            model_name='trees',
            name='Answer6',
            field=models.IntegerField(null=True, verbose_name='Answer6'),
        ),
        migrations.AddField(
            model_name='trees',
            name='Answer7',
            field=models.IntegerField(null=True, verbose_name='Answer7'),
        ),
        migrations.AddField(
            model_name='trees',
            name='Answer8',
            field=models.IntegerField(null=True, verbose_name='Answer8'),
        ),
        migrations.AddField(
            model_name='trees',
            name='Answer9',
            field=models.IntegerField(null=True, verbose_name='Answer9'),
        ),
        migrations.AlterField(
            model_name='trees',
            name='Answer1',
            field=models.IntegerField(null=True, verbose_name='Answer1'),
        ),
        migrations.AlterField(
            model_name='trees',
            name='Answer2',
            field=models.IntegerField(null=True, verbose_name='Answer2'),
        ),
        migrations.AlterField(
            model_name='trees',
            name='Answer3',
            field=models.IntegerField(null=True, verbose_name='Answer3'),
        ),
        migrations.AlterField(
            model_name='trees',
            name='Answer4',
            field=models.IntegerField(null=True, verbose_name='Answer4'),
        ),
        migrations.AlterField(
            model_name='trees',
            name='Answer5',
            field=models.IntegerField(null=True, verbose_name='Answer5'),
        ),
    ]
