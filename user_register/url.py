from django.conf.urls import url
from user_register import views

urlpatterns = [
    url('puserreg/', views.pstuserreg),
    url('vuserreg/', views.vwuserreg),
    url('aprvuser/(?P<idd>\w+)', views.approve, name='au'),
    url('rejuser/(?P<idd>\w+)', views.reject, name='ru')

]