from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# Create your views here.

def AUTHENTICATE(request):
    registration_submitted = True
    return render(request, 'auth/login_registation.html',{'registration_submitted':registration_submitted})



def Registration_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Already username exists!")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Already email exists!")
        else:
            if password != password1:
                messages.error(request, "Your password didn't match!")
            else:
                hashed_password = make_password(password)
                otp = randint(0000, 9999)
                user = CustomUser(username=username, profile_pic=image, email=email, password=hashed_password, otp=otp)
                user.save()
                subject = 'Your account verification OTP'
                message = f'Hi {user.username}, thank you for registering in Evara. Your OTP is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, 'Please check your mail for OTP')

    return redirect('login_registration')


def otp_verification(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp:
            user=CustomUser.objects.filter(otp=otp).first()
            if user:
                user.is_verified = True
                user.save()
                messages.success(request, 'OTP verification completed!')
            else:
                messages.error(request,'Invalid your OTP')
    return redirect('login_registration')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_verified:
                login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Please verify your account.')
        else:
            messages.error(request, 'Invalid username or password.')
    return redirect('login_registration')


def user_logout(request):
    logout(request)
    messages.success(request,'Successfuly logout your account')
    return redirect("login_registration")



def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            otp = randint(0000, 9999)
            user.otp = otp
            user.save()
            subject = 'Your password reset OTP'
            message = f'Hi {user.username}, your OTP for password reset is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request,'please cheack your mail !')
            return redirect('otp_verification', id=user.id)
        else:
            messages.error(request, 'No user found with that email address.')
    return render(request, 'auth/forgot.html')


def forgot_otp_verification(request,id):
    user = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp == user.otp:
            return redirect('reset_password_confirm', id=user.id)
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request, 'auth/otp_verify.html', {'user': user})


def reset_password_confirm(request,id):
    user = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            user = authenticate(username=user.username, password=new_password)
            login(request, user)
            messages.success(request, 'Password reset and loged in successful.')
            return redirect('home')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    return render(request, 'auth/forgot_confirm.html', {'user': user})



def PAGE_ACCOUNT(request):
    user = request.user
    address_obj = my_address.objects.filter(user=user)
    customer_obj = CustomUser.objects.get(username=user)
    return render(request, 'auth/page-account.html',{'address_obj':address_obj, 'customer_obj':customer_obj})




@login_required
def Account_details(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        npassword = request.POST.get('npassword')
        cpassword = request.POST.get('cpassword')
        user = CustomUser.objects.get(username=user)
        if user:
            if user.check_password(password):
                if npassword != cpassword:
                    messages.error(request, "Passwords didn't match!")
                else:
                    if not npassword:
                        user.first_name = first_name
                        user.last_name = last_name
                        user.phone_number = phone_number
                        user.email = email
                        user.save()
                        messages.success(request, 'Successfully saved your information!')
                        return redirect('dashboard')
                    else:
                        user.first_name = first_name
                        user.last_name = last_name
                        user.phone_number = phone_number
                        user.email = email
                        user.set_password(npassword)
                        user.save()
                        user = authenticate(username=user.username, password=npassword)
                        login(request, user)
                        messages.success(request, 'Successfully saved your information!')
                        return redirect('dashboard')
            else:
                messages.error(request,'invalid password !')
        else:
                messages.error(request,'user not found !')  
    return redirect('dashboard')

        
    
