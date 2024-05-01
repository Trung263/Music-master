from django.db import models
from django.urls import reverse

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    CATEGORY_CHOICES = (
        ('Nhạc Trẻ', 'Nhạc Trẻ'),
        ('Nhạc Dacce Việt', 'Nhạc Dacce Việt'),
        ('Rap Việt', 'Rap Việt'),
        ('ADM Việt', 'ADM Việt'),

    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,blank=True, null=True, default=None)
    image = models.FileField(upload_to='image/',unique=True)
    audio_file = models.FileField(upload_to='songs/',unique=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("appmusic:index")