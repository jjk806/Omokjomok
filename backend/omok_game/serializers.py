 
from rest_framework import serializers
from .models import *

class TrickSolvingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrickSolving
        firelds = ('game1', 'game2', 'game3', 'game4', 'game5',)