from django.conf.urls import url
from location import views

urlpatterns = [
    url('plocation/', views.pstlocation),
    url('vlocation/', views.vwlocation)


]