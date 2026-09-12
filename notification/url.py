from django.conf.urls import url
from notification import views

urlpatterns = [
    url('pnot/', views.pstnot),
    url('vnot/', views.vwnot)



]