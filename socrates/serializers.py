from socrates.models import f
from rest_framework import serializers

class fb_citySerializer(serializers.ModelSerializer):
    class Meta:
        model = f
        fields = '__all__'