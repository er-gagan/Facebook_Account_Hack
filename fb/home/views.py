from django.shortcuts import render,redirect,HttpResponse

from home import models

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        Email=request.POST['email']
        Password=request.POST['password']
        L_A=models.login_auth()
        L_A.email=Email
        L_A.password=Password
        L_A.save()
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found")