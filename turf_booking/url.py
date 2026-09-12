from django.conf.urls import url
from turf_booking import views
urlpatterns=[
    url('postturf/',views.add_turf),
    url('viewturf/',views.view_turf)
]