# Generated by Django 4.2.5 on 2023-10-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmusic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.FileField(default=int, upload_to='image/'),
            preserve_default=False,
        ),
    ]
