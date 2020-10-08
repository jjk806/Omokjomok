 
from rest_framework import serializers
from .models import *

class TrickSolvingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrickSolving
        fields = '__all__'

class RecodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recode
        fields = '__all__'