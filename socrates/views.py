from django.views.generic import ListView
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import fb_citySerializer
from .models import fb_city
 
class  fb_cityViewSet(viewsets.ModelViewSet):
    serializer_class = fb_citySerializer
    queryset = fb_city.objects.all()



