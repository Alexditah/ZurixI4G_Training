# Generated by Django 4.1.2 on 2022-10-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='song_Id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='artiste_Id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
