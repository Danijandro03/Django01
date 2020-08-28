from django.contrib import admin
from django.urls import path
from rest_framework import routers
from socrates.views import consultaViewSet
from socrates.serializers import consultaSerializer 
from django.urls import path, include

router = routers.SimpleRouter()

router.register(r'socrates', consultaViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls)  
]