from django.conf.urls import url
from delivery import views

urlpatterns = [
    url('del/(?P<idd>\w+)', views.pstdel),
    url('vdel/',views.vwdel)

]