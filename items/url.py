from django.conf.urls import url
from items import views

urlpatterns = [
    url('pitems/', views.add),
    url('vitems/', views.vwitems)

]