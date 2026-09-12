from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
# Create your views here.

def pstlogin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passew=request.POST.get('password')
        obj=Login.objects.filter(username=uname,password=passew)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.uid
            if tp=="admin":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp=="user":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/user/')
            elif tp=="clubmanager":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/clubmanager/')
            elif tp=="shop":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/shop/')
            elif tp=="trainer":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/trainer/')
        else:
            objlist = "Username or Password incorrect... Please try again...!"
            context = {
                'msg' : objlist,
                }

            return render(request,'login/post_login.html',context)
    return render(request,'login/post_login.html')



