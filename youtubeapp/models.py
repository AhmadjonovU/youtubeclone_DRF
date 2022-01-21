from django.db import models
from django.conf import settings

# Create your models here.
class Playlist(models.Model):
    title = models.CharField(max_length=70)
    video = models.FileField(upload_to="videos/Y")
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Comment(models.Model):
    matn = models.CharField(max_length=150)
    account = models.ForeignKey(settings.ACCOUNT_MODEL,related_name='user_comments',on_delete=models.CASCADE)
    sanasi = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(settings.ACCOUNT_MODEL, related_name="user_video", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.matn

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(settings.ACCOUNT_MODEL,related_name='yuser',on_delete=models.CASCADE)
    video = models.URLField()

    def __str__(self) -> str:
        return self.title