from django.conf.urls import url
from club import views

urlpatterns = [
    url('pclub/', views.pstclub),
    url('vclub/',views.vwclub),
    url('aprclub/(?P<idd>\w+)',views.approve),
    url('rejclub/(?P<idd>\w+)', views.reject)

]