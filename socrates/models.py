from django.db import models
#from django.core import serializers 
'''data = serializers.serialize('json', fb_city.objects.all())'''


class fb_city (models.Model):
    idcity = models.IntegerField() 
    idcountry = models.IntegerField()
    name = 'MIAMI'
    code = models.CharField(max_length=10)
    is_courrier = models.BooleanField()
    idstate = models.IntegerField() 
    isdelivery = models.BooleanField()
    active =models.BooleanField()
    consultado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 