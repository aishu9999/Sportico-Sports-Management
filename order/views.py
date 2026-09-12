from django.http import HttpResponseRedirect
from django.shortcuts import render
from order.models import Order
import datetime
from payment.models import Payment
from items.models import Product


# Create your views here.

def pstorder(request,idd):
    ss=request.session["uid"]
    ob = Product.objects.get(product_id=idd)
    context={
        'kk':ob
    }
    # if request.method=='POST':
    obb = Payment()
    obb.user_id = ss
    obb.method_cod_online_field = 'online'
    obb.amount = ob.price
    obb.cvv = '***'
    obb.date = datetime.datetime.now()
    obb.time = datetime.datetime.now()
    obb.save()

    obj=Order()
    obj.shop_id=ob.shop_id
    obj.product_id=ob.product_id
    obj.payment_id=obb.payment_id
    obj.user_id=ss
    obj.date=datetime.datetime.now()
    obj.time=datetime.datetime.now()
    obj.save()

    request.session['amt']=ob.price
    return HttpResponseRedirect('/payment/raz/#ff')
    # return render(request,'payment/payment.html',context)


def vworder(request):
    ss=request.session["uid"]
    obj = Order.objects.filter(shop_id=ss)
    context = {
        'x': obj,
    }
    return render(request,'order/view_order.html',context)

