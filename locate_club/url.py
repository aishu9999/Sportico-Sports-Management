from django.conf.urls import url
from locate_club import views

urlpatterns = [
    url('ploc/', views.pstloc),
    url('vloc/', views.vwloc)

]