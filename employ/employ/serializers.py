from dataclasses import field
import imp
from pyexpat import model
from .models import Emp
from rest_framework import serializers

class Empserializers(serializers.ModelSerializer):

    class Meta:
        model= Emp
        fields= ['id', 'name', 'desc']