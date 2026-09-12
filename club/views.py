from django.shortcuts import render
from club.models import Club
from login.models import Login

# Create your views here.

def pstclub(request):
    obk=""
    if request.method=='POST':
        obj=Club()
        obj.clubname=request.POST.get('clubname')
        obj.address= request.POST.get('address')
        obj.head=request.POST.get('head')
        obj.service=request.POST.get('service')
        obj.contact=request.POST.get('contact')
        obj.email_id=request.POST.get('email')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.save()

        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.type="clubmanager"
        ob.uid=obj.club_id
        ob.save()

        obk = "successfully registered"
    context = {
        'msg': obk
    }
    return render(request,'club/post_club.html',context)

def vwclub(request):
    obj = Club.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'club/view_club.html',context)

def approve(request,idd):
    obj=Club.objects.get(club_id=idd)
    obj.status='approve'
    obj.save()
    return vwclub(request)

def reject(request,idd):
    obj=Club.objects.get(club_id=idd).delete()
    ob=Login.objects.get(uid=idd,type='clubmanager')
    return vwclub(request)