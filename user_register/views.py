from django.shortcuts import render
from user_register.models import UserRegister
from login.models import Login
from django.db.models import Q
# Create your views here.

def pstuserreg(request):
    obk=""
    if request.method=='POST':
        a=request.POST.get('contact')
        U=request.POST.get('name')
        obv=UserRegister.objects.filter(Q(username=U)& Q(contact=a) | Q(contact=a))
        if len(obv)>0:
            obk="User With same phone number exist"
            context={
                'msg':obk
            }
            return render(request, 'user_register/post_user_register.html', context)
        else:
            obj=UserRegister()
            obj.username=request.POST.get('name')
            obj.age=request.POST.get('age')
            obj.gender=request.POST.get('gen')
            obj.address=request.POST.get('address')
            obj.height=request.POST.get('height')
            obj.weight=request.POST.get('weight')
            obj.physical=request.POST.get('physical')
            obj.contact=request.POST.get('contact')
            obj.email=request.POST.get('email')
            obj.password=request.POST.get('pass')
            obj.status='pending'
            obj.save()

            ob = Login()
            ob.username = obj.username
            ob.password = obj.password
            ob.type = "user"
            ob.uid = obj.user_id
            ob.save()
            obk="0"
            context={
                'msg':obk
            }
            return render(request,'user_register/post_user_register.html',context)
    return render(request,'user_register/post_user_register.html')

def vwuserreg(request):
    obj = UserRegister.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'user_register/view_user_register.html',context)

def approve(request,idd):
    obj=UserRegister.objects.get(user_id=idd)
    obj.status='approve'
    obj.save()
    return vwuserreg(request)

def reject(request,idd):
    obj=UserRegister.objects.get(user_id=idd)
    obj.status='reject'
    obj.save()
    return vwuserreg(request)

