from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customer
# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('accout_details')
def account(request):
    context={}
    # registers field
    try:
        if request.POST and 'register' in request.POST:
            
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #create user model
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            #create customer model
            customer=Customer.objects.create(
                user=user,
                address=address,
                phone_number=phone
                
            )
            success_message="user created successfully login to continue"
            messages.success(request,success_message)
            context['register']=False
            return redirect('accout_details')
    except Exception as e:
        context['register']=True
        error_message="duplicate user"
        messages.error(request,error_message)
    # login field
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            success_message="logedin successfully"
            messages.success(request,success_message)
            return redirect('home_page')
        else:
            error_message="bad credentials"
            messages.error(request,error_message)
    return render(request,'account.html',context)