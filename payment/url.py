from django.conf.urls import url
from payment import views

urlpatterns = [
    # url('ppay/(?P<idd>\w+)', views.pstpay),
    url('vpay/',views.vwpay),
    url('turfpay/(?P<idd>\w+)',views.pstpayment),
    url('raz/',views.homepage)


]