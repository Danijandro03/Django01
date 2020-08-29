from .models import fb_city
from rest_framework import serializers

class fb_citySerializer(serializers.ModelSerializer):
    class Meta:
        model = fb_city
        fields = '__all__'