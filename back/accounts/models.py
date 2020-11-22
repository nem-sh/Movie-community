from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail

class User(AbstractUser):
    critic = models.BooleanField(default=False)
    following_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower')
    follower_cnt = models.IntegerField(default=0)
    one_thing = models.CharField(max_length = 30 ,blank=True)
    name = models.CharField(max_length = 30 ,blank=True)
    img = ProcessedImageField(
                          processors=[Thumbnail(180,180)],
                          format='JPEG',
                          options={'quality': 80}
, blank=True)




class LikeUser(models.Model):
    
    you = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="you")
    me = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="me")
    like = models.IntegerField(default=0)