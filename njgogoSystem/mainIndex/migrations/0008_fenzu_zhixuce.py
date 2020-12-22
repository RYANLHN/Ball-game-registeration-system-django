# Generated by Django 3.1.3 on 2020-12-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainIndex', '0007_auto_20201201_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='fenzu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchid', models.IntegerField()),
                ('gametype', models.CharField(max_length=20)),
                ('zubie', models.IntegerField()),
                ('fenzuqk', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='zhixuce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchid', models.IntegerField()),
                ('gametype', models.CharField(max_length=20)),
                ('matchdetail', models.CharField(max_length=30)),
                ('lunshu', models.IntegerField()),
                ('zubie', models.IntegerField()),
            ],
        ),
    ]