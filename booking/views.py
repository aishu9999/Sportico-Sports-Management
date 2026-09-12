from django.shortcuts import render
from booking.models import Booking
from club.models import Club
from camp.models import Camp
from location.models import Location
from time_info.models import TimeInfo
from payment.models import Payment


# Create your views here.

def pstbook(request):
    ob=Club.objects.all()
    ob1=Camp.objects.all()
    ob2=Location.objects.all()
    ob3=TimeInfo.objects.all()
    ob4=Payment.objects.all()
    context={
        'x':ob,
        'y':ob1,
        'z':ob2,
        'w':ob3,
        'v':ob4,
    }
    if request.method=='POST':
        obj=Booking()
        obj.club_id=request.POST.get('cl')
        obj.user_id='1'
        obj.camp_id=request.POST.get('cm')
        obj.date=request.POST.get('date')
        obj.location_id=request.POST.get('lo')
        obj.time_id=request.POST.get('ti')
        obj.payment_id=request.POST.get('py')
        obj.save()
    return render(request,'booking/post_booking.html',context)

def vwbook(request):
    obj=Booking.objects.all()
    context={
        'x':obj,
    }
    return render(request,'booking/view_booking.html',context)

def vwbookusr(request):
    ss= request.session["uid"]
    obj=Booking.objects.filter(user_id=ss)
    context={
        'x':obj,
    }
    return render(request,'booking/view_bookin_user.html',context)
