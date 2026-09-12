from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from trainer_register.models import TrainerRegister
import datetime
from trainer_register.models import UploadedVideo
from login.models import Login

# Create your views here.

def psttrainreg(request):
    obk=""
    if request.method=='POST':
        obj=TrainerRegister()
        obj.name=request.POST.get('name')
        obj.gender=request.POST.get('gen')
        obj.field=request.POST.get('field')
        obj.time_info=request.POST.get('timeslot')
        obj.payment=request.POST.get('pay')
        obj.password=request.POST.get('pwd')
        obj.status='pending'
        obj.save()
        ob = Login()
        ob.username = obj.name
        ob.password = obj.password
        ob.type = "trainer"
        ob.uid = obj.trainer_id
        ob.save()

        obk="successfully registered"
    context={
        'msg':obk
    }

    return render(request,'trainer_register/post_trainer_register.html',context)

def vwtrainreg(request):
    obj = TrainerRegister.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'trainer_register/view_trainer_register.html',context)



def approve(request):
    ss=request.session["uid"]
    if request.method=='POST':
        obj=UploadedVideo()
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name, myfile)
        obj.video=myfile.name
        obj.trainer_id=ss
        obj.save()
    return render(request,'trainer_register/upload video.html')

def view(request):
    obj=UploadedVideo.objects.all()
    context={
        'kk':obj
    }
    return render(request,'trainer_register/Viewvideo.html',context)

def watch(request,idd):
    ob=UploadedVideo.objects.get(video_id=idd)
    context={
        'kk':ob
    }
    return render(request,'trainer_register/watch.html',context)

def trainer_view(request):
    obj=UploadedVideo.objects.all()
    context={
        'x':obj,
    }
    return render(request,'trainer_register/view_vdo_trainer.html',context)

def vdotrainer(request,idd):
    obj=UploadedVideo.objects.get(video_id=idd)
    obj.delete()
    return view(request)
