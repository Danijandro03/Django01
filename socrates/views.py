from django.views.generic import ListView
from django.shortcuts import render
from rest_framework import viewsets
from socrates.serializers import fb_citySerializer
from socrates.models import fb_city
 
f = fb_city(name='MIAMI')