from django.shortcuts import render
from camp.models import Camp
from club.models import Club
from booking.models import Booking
from django.http import HttpResponseRedirect

# Create your views here.

def pstcamp(request):
    obk=""
    ss=request.session["uid"]
    if request.method=='POST':
        obj=Camp()
        obj.club_id=ss
        obj.date=request.POST.get('date')
        obj.time=request.POST.get('time')
        obj.campname=request.POST.get('campname')
        obj.incharge=request.POST.get('incharge')
        obj.category=request.POST.get('category')
        obj.save()
        obk = "successfully registered"
    context = {
        'msg': obk
        }
    return render(request,'camp/post_camp.html',context)

def vwcamp(request):
    obj = Camp.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'camp/view_camp.html',context)

def bookcamp(request):
    obj = Camp.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'camp/bookcamp.html',context)

def campbookkk(request,idd):
    ss=request.session["uid"]
    ab=Camp.objects.get(camp_id=idd)
    obb=Booking()
    obb.camp_id=ab.camp_id
    obb.date=ab.date
    obb.time=ab.time
    obb.user_id=ss
    obb.club_id=ab.club_id
    obb.save()
    return bookcamp(request)

