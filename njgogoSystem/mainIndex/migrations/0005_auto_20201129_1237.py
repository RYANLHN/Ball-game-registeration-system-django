# Generated by Django 3.1.3 on 2020-11-29 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainIndex', '0004_auto_20201129_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerlist',
            name='contact',
            field=models.CharField(default=13247516283, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playerlist',
            name='contactNumber',
            field=models.IntegerField(default=13247516283),
            preserve_default=False,
        ),
    ]