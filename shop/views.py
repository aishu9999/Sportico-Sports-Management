from django.shortcuts import render
from shop.models import Shop
from login.models import Login

# Create your views here.

def pstshop(request):
    obk=""
    if request.method=='POST':
        obj=Shop()
        obj.shop_name=request.POST.get('shopname')
        obj.address=request.POST.get('add')
        obj.contact=request.POST.get('phone')
        obj.rating='0'
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.save()

        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.type = "shop"
        ob.uid = obj.shop_id
        ob.save()

        obk = "successfully registered"
    context = {
         'msg': obk
    }
    return render(request,'shop/post_shop.html',context)

def vwshop(request):
    obj = Shop.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'shop/view_shop.html',context)

def approve(request,idd):
    obj=Shop.objects.get(shop_id=idd)
    obj.status='approve'
    obj.save()
    return vwshop(request)

def reject(request,idd):
    obj=Shop.objects.get(shop_id=idd)
    obj.status='reject'
    obj.delete()
    return vwshop(request)

def vwshopuser(request):
    obj = Shop.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'shop/view_shop_user.html',context)
