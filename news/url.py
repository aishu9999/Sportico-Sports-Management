from django.conf.urls import url
from news import views

urlpatterns = [
    url('pnews/', views.pstnews),
    url('vnews/', views.vwnews)
    # url('aprnws/(?P<idd>\w+)',views.approve,name='apns'),
    # url('rejnws/(?P<idd>\w+)', views.reject,name='rjns')

]