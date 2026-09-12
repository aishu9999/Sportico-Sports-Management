from django.conf.urls import url
from turf_register import views

urlpatterns = [
    url('pturf/',views.pstturfreg),
    url('vturf/',views.vwturfreg),
    url('turfviewbook/',views.vturfff),
    url('bookturf/(?P<idd>\w+)',views.bookturf),
    # url('reject/(?P<idd>\w+)', views.reject, name='rjct'),

    url('map/(?P<idd>\w+)',views.map)



]