from django.shortcuts import render
from turf_booking.models import TurfBooking
import datetime
from club.models import Club
from location.models import Location
from time_info.models import TimeInfo
from turf_register.models import TurfRegister

# Create your views here.

def add_turf(request):
    ob = Club.objects.all()
    ob2 = Location.objects.all()
    ob3 = TimeInfo.objects.all()
    ob4=TurfRegister.objects.all()

    context = {
        'x': ob,
        'z': ob2,
        'w': ob3,
        'y': ob4,
    }
    if request.method=='POST':
        obj=TurfBooking()
        obj.user_id='1'
        obj.club_id=request.POST.get('cl')
        obj.turf_id=request.POST.get('tu')
        obj.location_id=request.POST.get('lo')
        obj.time_id=request.POST.get('ti')
        obj.date=datetime.datetime.now()
        obj.save()


    return render(request,'turf_booking/add_turf_booking.html',context)

def view_turf(request):
    obj=TurfBooking.objects.all()
    context={
        'x':obj,
    }
    return render(request,'turf_booking/view_turf_booking.html',context)
