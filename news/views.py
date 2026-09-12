from django.shortcuts import render
from news.models import News
import datetime
# Create your views here.

def pstnews(request):
    if request.method=='POST':
        obj=News()
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.title=request.POST.get('title')
        obj.content=request.POST.get('content')
        obj.status='pending'
        obj.save()
    return render(request,'news/post_news.html')

def vwnews(request):
    obj = News.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'news/view_news.html',context)

# def approve(request,idd):
#     obj=News.objects.get(news_id=idd)
#     obj.status='approve'
#     obj.save()
#     return vwnews(request)
#
# def reject(request,idd):
#     obj=News.objects.get(news_id=idd)
#     obj.status='reject'
#     obj.save()
#     return vwnews(request)


