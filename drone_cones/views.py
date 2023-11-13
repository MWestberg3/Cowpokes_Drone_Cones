from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import post_save
from drone_cones.core.forms import SignUpForm


# class LoginView:
#     def loginPage(request, email, user_password):
#         user = authenticate(username=email, password=user_password)
#         context = UserView.userDash()
#         if user is not None:
#             return render(request, 'drone_cones/login.html', context)
#         else:
#             return redirect_to_login('URL_GOES_HERE', 'LOGIN_URL')



class LoginView:
    def login(request):
        return render(request, 'drone_cones/login_page.html')

    def register(first_name, last_name, email, password):
        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect_to_login('URL_GOES_HERE', 'LOGIN_URL')
    
    def redirect_view(request):
        response = redirect('/dronecones/accounts/logout/')
        return response
        
    def logout():
        pass

    # @receiver(post_save, sender=User)
    def create_account(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                firstname = form.cleaned_data.get('firstname')
                user = authenticate(username=username, password=raw_password)
                login(request, user=user)
                return redirect('/dronecones/home/')
        else:
            form = SignUpForm()
        return render(request, "drone_cones/create_account_page.html", {'form': form})

class UserView:
    def view_cart():
        pass

    def view_profile():
        pass

    @login_required
    def user_dash(request):
        flavor_list = Products.objects.order_by('-type')
        context = {
            'flavor_list': flavor_list,
        }
        return render(request, 'drone_cones/home_page.html', context)

    @login_required
    def account_page(request):
        return render (request, 'drone_cones/account_page.html', {})
    
class DroneView:
    @login_required
    def drone_dash(request):
        drone_list = Drone.objects.order_by('-droneName')
        context = {
            'drone_list': drone_list,
        }
        return render(request, 'drone_cones/drone_page.html', context)

    def view_drones():
        pass

    @login_required
    def drone_register(request):
        return render(request, "drone_cones/drone_register_page.html")

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

    @login_required
    def order_page(request):
        product_list = reversed(Products.objects.order_by("-id"))
        stock_list = reversed(Products.objects.order_by("-stockAvailable"))
        context = {'productList': product_list, 'stockAvailable': stock_list}
        return render(request, 'drone_cones/order_page.html', context)

    @login_required
    def order_confirmation(request):
        orders = reversed(Orders.objects.order_by("-id"))
        context = {'orders': orders}
        return render(request, 'drone_cones/confirmation_page.html', context)

    def edit_address():
        pass

    def add_address():
        pass
