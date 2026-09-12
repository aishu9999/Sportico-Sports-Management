from django.shortcuts import render
from time_info.models import TimeInfo
from club.models import Club

import datetime

# Create your views here.

# def psttimeinfo(request):
#     if request.method=='POST':
#         obj=TimeInfo()
#         obj.club_id='1'
#         obj.time=request.POST.get('tslot')
#         obj.save()
#     return render(request,'time_info/post_time_info.html')


def timeinfo(request):
    ob = Club.objects.all()

    context={
        'x':ob,
    }
    if request.method=="POST":
        ob=TimeInfo()
        ob.club_id=request.POST.get('cl')
        ob.time_info=request.POST.get('t1')
        ob.save()
    return render(request,'time_info/post_time_info.html',context)

def vwtimeinfo(request):
    obj = TimeInfo.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'time_info/view_time_info.html',context)


