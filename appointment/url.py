from django.conf.urls import url
from appointment import views

urlpatterns=[
    url('papp/(?P<idd>\w+)',views.pstapp),
    url('vapp/',views.vwapp)

]