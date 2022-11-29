from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,'index.html',{})
def About(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def gall(request):
    return render(request,'gallery.html',{})

def reser(request):
    return render(request,'reservation.html',{})

def contactdata(request):
    firstname=request.POST.get('fname','default')
    mobile=request.POST.get('mob','default')
    Email=request.POST.get('mail','default')
    Message=request.POST.get('msg','default')
    con=Contact(first_name=firstname,Mob_no=mobile,textmsg=Message)
    con.save()
    print(firstname,mobile,Email,Message)
    return HttpResponse("Thanks for contact us..")

def reservation_data(request):
    firstname=request.POST.get('fname','default')
    Mobile_no=request.POST.get('Mobile_No','default')
    Email=request.POST.get('mailid','defalut')
    check_in=request.POST.get('checkin','default')
    check_out=request.POST.get('checkout','default')
    subject="Reservation details"
    message=f"Name:{firstname}'\n' Mobile:{Mobile_no}'\n'Mail:{Email}'\n'checkin:{check_in}'\n'checkout:{check_out}"
    Email_from=settings.EMAIL_HOST_USER
    send_mail(subject,message,Email_from,['as9771184@gmail.com'])
    return HttpResponse ("thanks for Reservation enquiry us..<a href='/'>Click here </a> for homepage")

def signupdata(request):
    username=request.POST.get('uname','default')
    firstname=request.POST.get('fname','default')
    Mail=request.POST.get('mail','default')
    Password=request.POST.get('pass','default')
    userexist=User.objects.filter(username=username)
    if userexist:
        return HttpResponse("username already exists")
    else:
        user=User.objects.create(username=username,first_name=firstname,email=Mail,password=Password)
        user.set_password(Password)
        user.save()
        return render(request,'login.html',{})
   
def sign(request):
    return render(request,'signup.html',{})

def login(request):
    return render(request,'login.html',{})

def logindata(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request)
            return render(request,'index.html',{})
        return HttpResponse("you enter invalid username or password")

def room(request):
    return render(request,'room.html',{})