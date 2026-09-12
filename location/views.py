from django.shortcuts import render
from location.models import Location
from club.models import Club


# Create your views here.

def pstlocation(request):
    ob = Club.objects.all()

    context = {
        'x': ob,
    }
    if request.method=='POST':
        obj=Location()
        obj.club_id=request.POST.get('cl')
        obj.latitude=request.POST.get('latitude')
        obj.longitude=request.POST.get('longitude')
        obj.save()
    return render(request,'location/post_location.html',context)

def vwlocation(request):
    obj = Location.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'location/view_location.html',context)


