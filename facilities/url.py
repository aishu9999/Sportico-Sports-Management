from django.conf.urls import url
from facilities import views

urlpatterns = [
    url('pfac/',views.pstfac),
    url('vfac/',views.vwfac)

]