from django.conf.urls import url
from chat import views

urlpatterns=[
    url('vc/',views.user),
    url('ad/(?P<idd>\w+)',views.adchat),
    url('tr/',views.train),
    url('ch/(?P<idd>\w+)',views.trhat),

]