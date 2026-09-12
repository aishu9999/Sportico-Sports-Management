from django.shortcuts import render
from user_register.models import UserRegister
from trainer_register.models import TrainerRegister
from chat.models import Chat
from django.db.models import Q
import datetime
# Create your views here.
from login.models import Login


def user(request):
    ob= TrainerRegister.objects.all()
    context={
        'aa':ob
    }
    return render(request,'chat/view user.html',context)

def adchat(request,idd):
    ss=request.session["uid"]
    obj = TrainerRegister.objects.get(trainer_id=idd)
    ob = Chat.objects.filter(Q(trainer_id=idd) & Q(user_id=ss))
    context = {
        'kk': ob,
        'uu': obj,
    }

    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.trainer_id=idd
        obk.user_id=ss
        # obk.date = datetime.date.today()
        # obk.time = datetime.datetime.now()
        obk.rectype="trainer"
        obk.sendertype ="user"
        obk.save()
    return render(request, 'chat/chatuser1.html',context)

def train(request):
    ob= UserRegister.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/trainer.html',context)

def trhat(request,idd):
    ss = request.session["uid"]
    obj = UserRegister.objects.get(user_id=idd)
    ob = Chat.objects.filter(Q(trainer_id=ss) & Q(user_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }

    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.trainer_id = ss
        obk.user_id = idd
        # obk.date = datetime.date.today()
        # obk.time = datetime.datetime.now()
        obk.rectype = "user"
        obk.sendertype = "trainer"
        obk.save()
    return render(request, 'chat/chatuser2.html',context)
