from django.shortcuts import render
from emergency_number.models import EmergencyNumber

# Create your views here.

def pstemnum(request):
    if request.method=='POST':
        obj=EmergencyNumber()
        obj.name=request.POST.get('name')
        obj.contact=request.POST.get('phone')
        obj.service=request.POST.get('service')
        obj.save()
    return render(request,'emergency_number/post_emergency_number.html')

def vwemnum(request):
    obj = EmergencyNumber.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'emergency_number/view_emergency_number.html',context)

