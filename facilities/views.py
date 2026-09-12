from django.shortcuts import render
from facilities.models import Facilities
from club.models import Club
from time_info.models import TimeInfo
import datetime

# Create your views here.

def pstfac(request):
    ss=request.session["uid"]
    if request.method=='POST':
        obj=Facilities()
        obj.club_id=ss
        obj.time=datetime.datetime.now()
        obj.equipments=request.POST.get('equipment')
        obj.services=request.POST.get('service')
        obj.games=request.POST.get('games')
        obj.save()
    return render(request,'facilities/post_facilities.html')

def vwfac(request):
    obj = Facilities.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'facilities/view_facilities.html',context)

