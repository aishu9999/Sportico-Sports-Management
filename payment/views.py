from django.shortcuts import render
from payment.models import Payment
from shop.models import Shop
from turf_booking.models import TurfBooking
from django.http import HttpResponseRedirect, HttpResponse
import datetime
# Create your views here.

# def pstpay(request,idd):
#     ob=Shop.objects.get(shop_id=idd)
#     a=ob.price
#     context={
#         'k':a
#     }
#     if request.method=='POST':
#         obj=Payment()
#         obj.user_id='1'
#         obj.method_cod_online_field=request.POST.get('method')
#         obj.amount=a
#         obj.cvv = request.POST.get('cvv')
#         obj.date=datetime.datetime.now()
#         obj.time=datetime.datetime.now()
#         obj.save()
#         return HttpResponseRedirect('/shop/usrshop/')
#     return render(request,'payment/post_payment.html',context)

def vwpay(request):
    obj = Payment.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'payment/view_payment.html',context)


def pstpayment(request,idd):
    context={
        'k':idd
    }
    if request.method=='POST':
        obj=Payment()
        obj.user_id='1'
        obj.method_cod_online_field=request.POST.get('method')
        obj.cvv=request.POST.get('cvv')
        obj.amount=idd
        obj.date=datetime.datetime.now()
        obj.time=datetime.datetime.now()
        obj.save()
        return HttpResponseRedirect('/turf_register/turfviewbook/')
    return render(request,'payment/payment.html',context)



import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def homepage(request):

    currency = 'INR'
    amt=int(request.session['amt'])*100
    amount =  amt # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '/temp/user/#aa/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'payment/rpay.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
    amt = int(request.session['amt']) * 100
    # only accept POST request.
    if request.method == "POST":
        try:

            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                amount = amt # Rs. 200
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    return HttpResponse('success')
                    # return HttpResponseRedirect('/turf_register/turfviewbook/')
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()
        # return HttpResponseRedirect('/turf_register/turfviewbook/')

