from django.conf.urls import url
from emergency_number import views

urlpatterns = [
    url('pemnum/',views.pstemnum),
    url('vemnum/',views.vwemnum)

]