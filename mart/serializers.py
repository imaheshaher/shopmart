from rest_framework import serializers
from . models import *

class ShopSerializer(serializers.ModelSerializer):
  class Meta:
    model=Category    
    fields='__all__'
    