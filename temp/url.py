from django.conf.urls import url
from temp import views

urlpatterns=[
    url('home/',views.home),
    url('admin/',views.admin),
    url('clubmanager/',views.clubmanager),
    url('shop/',views.shop),
    url('trainer/',views.trainer),
    url('user/',views.user),
]