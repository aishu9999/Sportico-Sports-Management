from django.shortcuts import render
from turf_register.models import TurfRegister
from turf_booking.models import TurfBooking
from django.http import HttpResponseRedirect
from payment.models import Payment
import datetime
# Create your views here.

def pstturfreg(request):
    obk=""
    if request.method=='POST':
        obj=TurfRegister()
        obj.name=request.POST.get('name')
        obj.place = request.POST.get('place')
        obj.email = request.POST.get('email')
        obj.contactno = request.POST.get('contactno')
        obj.amount = request.POST.get('amount')
        obj.lat = request.POST.get('lat')
        obj.lon = request.POST.get('lon')

        obj.save()

        obk = "successfully registered"
    context = {
        'msg': obk
     }

    return render(request,'turf_register/post_turf.html',context)

def vwturfreg(request):
    obj=TurfRegister.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'turf_register/view_turf.html',context)

def vturfff(request):
    obj=TurfRegister.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'turf_register/turfviewbook.html',context)

def bookturf(request,idd):
    ss=request.session["uid"]
    ab=TurfRegister.objects.get(turf_id=idd)
    # context={
    #     'kk':ab
    # }
    # if request.method=="POST":
    obv=Payment()
    obv.user_id=ss
    obv.date=datetime.datetime.today()
    obv.time=datetime.datetime.now()
    obv.amount=ab.amount
    obv.save()
    request.session['amt']=ab.amount

    obb=TurfBooking()
    obb.turf_id=idd
    obb.date=datetime.datetime.now()
    obb.user_id=ss
    obb.save()
    return HttpResponseRedirect('/payment/raz/#ff')
    # return render(request,'payment/post_payment.html',context)

def map(request,idd):
    ss=request.session["uid"]
    ab=TurfRegister.objects.get(turf_id=idd)
    context={
        'lat':ab.lat,
        'lon':ab.lon
    }
    print(ab.lat)
    print(ab.lon)
    return render(request,'turf_register/mapviewsports.html',context)




