from django.db import models
from django.conf import settings

# Create your models here.

class TrickSolving(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game1 = models.BooleanField(default=False)
    game2 = models.BooleanField(default=False)
    game3 = models.BooleanField(default=False)
    game4 = models.BooleanField(default=False)
    game5 = models.BooleanField(default=False)
