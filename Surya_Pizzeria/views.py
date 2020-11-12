from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from.models import Pizza_Data

# Create your views here.

def adminhomepageview(request):
    pizzas = Pizza_Data.objects.all()
    context = {'data': pizzas}
    return render(request, 'admin home page.html', context)

def adminloginview(request):
    return render(request, 'admin login page.html')

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None and user.username == 'admin':
        login(request, user)
        return redirect(adminhomepageview)
    else:
        messages.add_message(request, messages.ERROR,
                             message="Invaild credentials")
        return redirect(adminloginview)

def adminlogout(request):

    logout(request)
    return redirect(adminloginview)

def addpizza(request):
    pizza_name = request.POST['pizza']
    pizza_price = request.POST['price']
    if '' not in (pizza_price, pizza_name):
        Pizza_Data(pizza_name=pizza_name, pizza_price=pizza_price).save()
    else:
        messages.add_message(request, messages.ERROR,
                             message='Enter all details')
    return redirect(adminhomepageview)

def deletepizza(request, pizza_num):
    Pizza_Data.objects.filter(id=pizza_num).delete()
    return redirect(adminhomepageview)

def customerhomepage(request):

    return render(request,'customer home page.html')

def customerloginview(request):
    return render(request,'customer login page.html')

def  customersignuppage(request):
    return render(request,'customer signup page.html')
