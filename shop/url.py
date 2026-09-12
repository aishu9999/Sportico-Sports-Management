from django.conf.urls import url
from shop import views

urlpatterns = [
    url('pshop/', views.pstshop),
    url('vshop/', views.vwshop),
    url('apr/(?P<idd>\w+)',views.approve),
    url('rjctshop/(?P<idd>\w+)',views.reject),
    url('usrshop/',views.vwshopuser)



]