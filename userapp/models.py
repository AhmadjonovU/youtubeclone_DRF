from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Kanal(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=150,blank=True)
    profile_pic = models.URLField(blank = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    obunachilar = models.ManyToManyField(settings.ACCOUNT_MODEL, related_name = 'user_obunachilar',blank=True,symmetrical = False)
    obunalar = models.ManyToManyField(settings.ACCOUNT_MODEL, related_name = 'user_obunalar',blank=True,symmetrical = False)

    def count_obunachilar(self):
        if self.obunachilar.count() > 0:
            return self.obunachilar.count()
        else:
            return 0

    def count_obunalar(self):
        if self.obunachilar.count() > 0:
            return self.obunachilar.count()
        else:
            return 0

    def __str__(self):
        return self.user.username
