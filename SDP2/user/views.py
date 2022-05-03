from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .forms import RegistrationForm,ContentForm
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import User
from django.db.models import Q
import random


def strength_generator():
    rand=random.randint(10000, 200000)
    return rand

def userregistration(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Welcome to GetYourGoods.'
            message = "Thank you for registering in our website."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,'register.html',{'form':form})
def loginpage(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        flag=User.objects.filter(Q(username=uname) & Q(password=pwd))
        if flag:
            request.session['uname']=uname
            return redirect('service')
        else:
            return HttpResponse("Login Invalid")
    return render(request,"login.html")
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def products(request):
    return render(request,"products.html")
def footware(request):
    return render(request,"footware.html")
def clothing(request):
    return render(request,"clothing.html")
def fitnessandsports(request):
    return render(request,"fitnessandsports.html")
def homedecor(request):
    return render(request,"homedecor.html")
def electronics(request):
    return render(request,"electronics.html")
def groceriesandfood(request):
    return render(request,"groceries.html")
def cart(request):
    return render(request,"cart.html")
def order(request):
    return render(request,"order.html")
def checkout(request):
    if request.method == 'POST':
        form1 = ContentForm(request.POST)
        if form1.is_valid():
            form1.save()
            subject = 'Thank You for Placing your order.'
            message = "Your coupon code is " + str(strength_generator())+" Show this mail and redeem it your nearest stores."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form1.cleaned_data['email']]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('order')
    else:
        form1= ContentForm()
    return render(request, 'checkout.html', {'form': form1})
def phnpe(request):
    return render(request, "phnpe.html")
def gpay(request):
    return render(request,"gpay.html")
def index1(request):
    return render(request,"index1.html")


