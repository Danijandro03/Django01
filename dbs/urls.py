from django.contrib import admin
from django.urls import path
from rest_framework import routers
from socrates.views import f
from socrates.serializers import fb_citySerializer
from django.urls import path, include

router = routers.SimpleRouter()

router.register(r'socrates', f)

urlpatterns = router.urls 

urlpatterns += [
    path('admin/', admin.site.urls)
]
