# Generated by Django 2.0.6 on 2018-10-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20180925_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_format',
            field=models.CharField(default='audio/mp3', max_length=64),
        ),
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.FloatField(default=0.0, max_length=64),
        ),
        migrations.AddField(
            model_name='song',
            name='size',
            field=models.FloatField(default=0.0, max_length=64),
        ),
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ManyToManyField(to='songs.Genre'),
        ),
    ]
