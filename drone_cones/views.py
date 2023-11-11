from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.views import redirect_to_login
from django.template import loader


def createAccount(request):
    return render(request, "drone_cones/create_account_page.html")

def droneRegister(request):
    return render(request, "drone_cones/drone_register_page.html")

def dronePage(request):
    return render(request, "drone_cones/drone_page.html", {})

def orderPage(request):
    product_list = reversed(Products.objects.order_by("-id"))
    stock_list = reversed(Products.objects.order_by("-stockAvailable"))
    context = {'productList': product_list, 'stockAvailable': stock_list}
    return render(request, "drone_cones/order_page.html", context)

def homePage(request):
    return render(request, 'drone_cones/home_page.html', {})

def accountPage(request):
    return render(request, 'drone_cones/account_page.html', {})

def orderConfirmation(request):
    orders = reversed(Orders.objects.order_by("-id"))
    context = {'orders': orders}
    return render(request, 'drone_cones/confirmation_page.html', context)

class LoginView:
    def loginPage(request, email, user_password):
        user = authenticate(username=email, password=user_password)
        context = UserView.userDash()
        if user is not None:
            return render(request, 'drone_cones/login.html', context)
        else:
            return redirect_to_login('URL_GOES_HERE', 'LOGIN_URL')


    def register(first_name, last_name, email, password):
        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect_to_login('URL_GOES_HERE', 'LOGIN_URL')
        
    def logout():
        pass

class UserView:
    def view_cart():
        pass

    def view_profile():
        pass

    def user_dash(request):
        flavor_list = Products.objects.order_by('-type')
        context = {
            'flavor_list': flavor_list,
        }
        #return render(request, 'URL_GOES_HERE', context)

class DroneView:
    def drone_dash(request):
        drone_list = Drone.objects.order_by('-droneName')
        context = {
            'drone_list': drone_list,
        }
        return render(request, 'URL_GOES_HERE', context)

    def view_drones():
        pass

    def edit_drones():
        pass

class AdminView:
    def admin_dash():
        pass

    def view_users():
        pass

    def edit_users():
        pass

class OrderView:
    def order_view():
        pass

    def edit_address():
        pass

    def add_address():
        pass
