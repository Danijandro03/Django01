from django.views.generic import ListView
from django.shortcuts import render
from rest_framework import viewsets
from socrates.serializers import consultaSerializer
from socrates.models import consulta

class  consultaViewSet(viewsets.ModelViewSet):
    serializer_class = consultaSerializer
    queryset = consulta.objects.all()



