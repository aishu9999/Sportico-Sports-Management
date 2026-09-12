from django.conf.urls import url
from order import views

urlpatterns = [
    url('porder/(?P<idd>\w+)', views.pstorder),
    url('vorder/', views.vworder)

]