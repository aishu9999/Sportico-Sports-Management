from django.shortcuts import render
from appointment.models import Appointment
from trainer_register.models import TrainerRegister
# from payment.models import Payment


# Create your views here.
def pstapp(request,idd):
    ss=request.session["uid"]
    # ob=TrainerRegister.objects.all()
    # # ob1=Payment.objects.all()
    # context={
    #     'x':ob,
    #     # 'y':ob1,
    #
    # }
    if request.method=='POST':
        obj=Appointment()
        obj.user_id=ss
        obj.trainer_id=idd
        # obj.payment_id=request.POST.get('py')
        obj.date=request.POST.get('dt')
        obj.time=request.POST.get('tm')
        obj.save()
    return render(request,'appoinment/post_appointment.html')


def vwapp(request):
    ss=request.session["uid"]
    obj=Appointment.objects.filter(trainer_id=ss)
    context={
        'x':obj,
    }
    return render(request,'appoinment/view_appointment.html',context)
