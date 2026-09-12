from django.conf.urls import url
from time_info import views

urlpatterns =[
    url('post/', views.timeinfo),
    url('vtimeinfo/', views.vwtimeinfo)

]