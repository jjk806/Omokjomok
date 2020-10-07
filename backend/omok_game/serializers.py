 
from rest_framework import serializers
from .models import *

class TrickSolvingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrickSolving
        fields = '__all__'