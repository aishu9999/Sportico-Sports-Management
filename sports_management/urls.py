"""sports_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views
from payment import views as pview
urlpatterns = [
    path('admin/', admin.site.urls),
    url('appointment/',include('appointment.url')),
    url('booking/',include('booking.url')),
    url('camp/',include('camp.url')),
    url('chat/',include('chat.url')),
    url('club/',include('club.url')),
    url('delivery/',include('delivery.url')),
    url('emergency_number/',include('emergency_number.url')),
    url('facilities/',include('facilities.url')),
    url('items/',include('items.url')),
    url('locate_club/',include('locate_club.url')),
    url('location/',include('location.url')),
    url('login/',include('login.url')),
    url('news/',include('news.url')),
    url('notification/',include('notification.url')),
    url('order/',include('order.url')),
    url('payment/',include('payment.url')),
    url('shop/',include('shop.url')),
    url('time_info/',include('time_info.url')),
    url('trainer_register/',include('trainer_register.url')),
    url('user_register/',include('user_register.url')),
    url('turf_booking/',include('turf_booking.url')),
    url('turf_register/',include('turf_register.url')),
    url('temp/',include('temp.url')),
    path('pay/', pview.homepage, name='index'),
    path('paymenthandler/', pview.paymenthandler, name='paymenthandler'),
    url('$',views.pstlogin),

]
