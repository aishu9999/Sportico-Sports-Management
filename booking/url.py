from django.conf.urls import url
from booking import views

urlpatterns = [
    url('pbook/',views.pstbook),
    url('vbook/',views.vwbook),
    url('bkvwusr/',views.vwbookusr)

]