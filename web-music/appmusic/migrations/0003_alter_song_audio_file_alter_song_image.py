# Generated by Django 4.2.5 on 2023-10-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmusic', '0002_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(unique=True, upload_to='songs/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.FileField(unique=True, upload_to='image/'),
        ),
    ]
