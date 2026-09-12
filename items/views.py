from django.shortcuts import render
from items.models import Items
from items.models import Product


# Create your views here.

def add(request):
    ss=request.session["uid"]
    if request.method=='POST':
        ob=Product()
        ob.name=request.POST.get('name')
        ob.price=request.POST.get('price')
        ob.rentpurchase=request.POST.get('rp')
        ob.shop_id=ss
        ob.save()

    return render(request,'items/post_items.html')
def vwitems(request):
    obj = Product.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'items/view_items.html',context)

