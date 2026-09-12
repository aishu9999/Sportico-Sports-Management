from django.shortcuts import render
from delivery.models import Delivery
from shop.models import Shop
from order.models import Order

# Create your views here.

def pstdel(request,idd):
    ss=request.session["uid"]
    obv=Order.objects.get(order_id=idd)
    if request.method=='POST':
        obj=Delivery()
        obj.shop_id=ss
        obj.delivery_status=request.POST.get('dlvy')
        obj.date=request.POST.get('dt')
        obj.time=request.POST.get('tm')
        obj.user_id=obv.user_id
        obj.order_id=idd
        obj.save()
    return render(request,'delivery/post_delivery.html')

def vwdel(request):
    ss=request.session["uid"]

    obj = Delivery.objects.filter()
    context = {
        'x': obj,
    }
    return render(request,'delivery/view_delivery.html',context)

