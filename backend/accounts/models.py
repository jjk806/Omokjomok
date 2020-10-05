from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(unique=True, blank=False)
	win = models.IntegerField(default=0)
	lose = models.IntegerField(default=0)
	rate = models.IntegerField(default=0)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		db_table="Users"