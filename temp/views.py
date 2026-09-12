from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp/home.html')

def admin(request):
    return render(request, 'temp/admin.html')

def clubmanager(request):
    return render(request, 'temp/Club Manager.html')

def shop(request):
    return render(request, 'temp/Shop.html')

def trainer(request):
    return render(request, 'temp/Trainer.html')

def user(request):
    return render(request, 'temp/User.html')


