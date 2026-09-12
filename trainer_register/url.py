from django.conf.urls import url
from trainer_register import views

urlpatterns = [
    url('ptrainreg/', views.psttrainreg),
    url('vtrainreg/', views.vwtrainreg),
    url('app/',views.approve),
    url('view/',views.view),
    url('watch/(?P<idd>\w+)',views.watch),
    url('trai',views.trainer_view),
    url('delete/(?P<idd>\w+)',views.vdotrainer,name='xx')



]