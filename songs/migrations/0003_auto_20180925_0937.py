# Generated by Django 2.0.6 on 2018-09-25 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_song_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='songs.Artist'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]