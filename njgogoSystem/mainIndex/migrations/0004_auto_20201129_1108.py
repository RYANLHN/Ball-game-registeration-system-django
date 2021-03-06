# Generated by Django 3.1.3 on 2020-11-29 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainIndex', '0003_gametype'),
    ]

    operations = [
        migrations.CreateModel(
            name='playerlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchid', models.IntegerField()),
                ('playerCompany', models.CharField(max_length=20)),
                ('playerType', models.CharField(max_length=10)),
                ('player1Name', models.CharField(max_length=8)),
                ('player1Id', models.IntegerField()),
                ('player2Name', models.CharField(max_length=8)),
                ('player2Id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Gametype',
        ),
    ]
