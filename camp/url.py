from django.conf.urls import url
from camp import views

urlpatterns = [
    url('pcamp/',views.pstcamp),
    url('vcamp/',views.vwcamp),
    url('cabook/',views.bookcamp),
    url('bk/(?P<idd>\w+)',views.campbookkk)


]