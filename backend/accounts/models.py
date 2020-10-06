from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(unique=True, blank=False)
	play = models.IntegerField(default=0) # AI 대전 횟수
	win = models.IntegerField(default=0) # AI 대전 승
	rate = models.FloatField(default=0) # AI 대전 승/ 횟수
	score = models.IntegerField(default=0) # 묘수풀이 점수

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		db_table="Users"