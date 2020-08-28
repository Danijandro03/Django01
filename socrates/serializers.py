from rest_framework import serializers
from .models import consulta


class consultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = consulta
        fields = '__all__'