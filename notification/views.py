from django.shortcuts import render
from notification.models import Notification
import datetime
from club.models import Club

# Create your views here.

def pstnot(request):
    ob = Club.objects.all()

    context = {
        'x': ob,
    }
    if request.method=='POST':
        obj=Notification()
        obj.time=datetime.datetime.now()
        obj.date=datetime.datetime.now()
        obj.club_id=request.POST.get('cl')
        obj.notification=request.POST.get('notification')
        obj.save()
    return render(request,'notification/post_notification.html',context)

def vwnot(request):
    obj = Notification.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'notification/view_notification.html',context)


