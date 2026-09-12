from django.shortcuts import render
from locate_club.models import LocateClub
from club.models import Club


# Create your views here.

def pstloc(request):
    ob=Club.objects.all()

    context={
        'x':ob,
    }
    if request.method=='POST':
        obj=LocateClub()
        obj.club_id=request.POST.get('cl')
        obj.location=request.POST.get('location')
        obj.save()
    return render(request,'locate_club/post_locate_club.html',context)

def vwloc(request):
    obj = LocateClub.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'locate_club/view_locate_club.html',context)

