# Generated by Django 3.1.3 on 2020-12-01 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainIndex', '0006_auto_20201129_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchlist',
            name='matchBMtype',
            field=models.CharField(default=11, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='matchlist',
            name='matchtype',
            field=models.CharField(max_length=60),
        ),
    ]