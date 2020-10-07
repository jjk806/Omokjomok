from django.db import models
from django.conf import settings

# Create your models here.

class TrickSolving(models.Model):
    user = models.IntegerField()
    game1_1 = models.IntegerField(default=0)
    game1_2 = models.IntegerField(default=0)
    game1_3 = models.IntegerField(default=0)
    game1_4 = models.IntegerField(default=0)
    game1_5 = models.IntegerField(default=0)
    game2_1 = models.IntegerField(default=0)
    game2_2 = models.IntegerField(default=0)
    game2_3 = models.IntegerField(default=0)
    game2_4 = models.IntegerField(default=0)
    game2_5 = models.IntegerField(default=0)
    game3_1 = models.IntegerField(default=0)
    game3_2 = models.IntegerField(default=0)
    game3_3 = models.IntegerField(default=0)
    game3_4 = models.IntegerField(default=0)
    game3_5 = models.IntegerField(default=0)


class omokgame(models.Model):
    gid = models.AutoField(db_column = 'gid', primary_key = True)
    data = models.TextField(db_column = 'data')
    auid = models.IntegerField(db_column = 'auid')
    turn = models.IntegerField(db_column = 'turn')
    date = models.DateTimeField(db_column = 'date')

    class Meta:
        db_table = 'game'


class myosu(models.Model):
    mid = models.AutoField(db_column = 'mid', primary_key = True)
    data = models.TextField(db_column = 'data')
    round = models.IntegerField(db_column = 'round')

    class Meta:
        db_table = 'myosu'


class room(models.Model):
     rid = models.AutoField(db_column = 'rid', primary_key = True)
     uid = models.IntegerField(db_column = 'uid')
     att_turn = models.IntegerField(db_column = 'att_turn', default = 0)
     level = models.IntegerField(db_column = 'level')

     class Meta:
        db_table = 'room'