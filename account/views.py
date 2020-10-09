from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout,  authenticate
from .forms import UserCreationForm, UserLoginForm, UserProfileEdithForm, EmailAddressChangeForm, UserWithdrawRequestForm, UserDepositRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import random
from django.core.mail import EmailMessage
from django.core.mail import send_mail


from django.template import Context
from django.template.loader import render_to_string, get_template

from account.models import User, ManagerWalletAddress, UserDepositRequest, UserWithdrawRequest, Account_level
user = User.objects.all()


main_otp = 0



def Signup_view(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')
    else:
    
        if request.method == 'POST':
            form = UserCreationForm(request.POST, request.FILES)
            if form.is_valid():

            
                form.save()
            
                to = form.cleaned_data.get('email')
                subject = '27Cryptotrading Account'
                first_name = form.cleaned_data.get('first_name')
                message = 'Hi {} a verification code will be sent to your registered email address shortly use the code to activate your 27cryptotrading account'.format(first_name)
            
               
                recipient_list = [to,]    
                send_mail( subject, message, '27Cryptotrading noreply@27cryptotrading.com', recipient_list ) 

                email  = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password2')
                user = authenticate(email=email, password=password)
                

                if user:
                    login(request, user)

                    messages.success(request, "Welcome {} your account was created successfully".format(first_name))
                    return redirect('send_otp')

            
        else:
            form = UserCreationForm()
        return render(request, 'account/register.html', {'form':form})





def login_view(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')

    

    
    else:

        if request.POST:
            form = UserLoginForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(email=email, password=password)
                

                if user:
                    login(request, user)
                    messages.success(request, "Welcome {} ".format(request.user.first_name))
                    
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        
                        return redirect('user_dashboard')
                    
        
                    
        else:
            form = UserLoginForm()
        return render(request, 'account/login.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('home_page')


@login_required(login_url='login')
def personal_info(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    

    context = {}
    user = request.user
    
    if request.POST:
        user = request.user
        form = UserProfileEdithForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Hi {} Your Account has been  successfully updated!".format(request.user.first_name))
            return redirect('send_otp')

    else:
        form = UserProfileEdithForm(initial = {
                                                "first_name": request.user.first_name,
                                                "last_name": request.user.last_name,
                                                "phone": request.user.phone
                                                })
    
    context = {
        'form': form,
       
    }
    return render(request, 'account/personal_info.html', context)


@login_required(login_url='login')
def user_dashboard(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    if request.user.is_admin:
        return redirect('home_page')
    
    
    
        
    
   
    


   

    return render(request, 'account/dashboard.html')

@login_required(login_url='login')
def withdraw_not_eligable(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    
    if request.user.is_admin:
        return redirect('home_page')

    return render(request, 'account/withdraw_not_eligable.html')


@login_required(login_url='login')
def withdraw_complete_error(request):
    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')

    return render(request, 'account/withdraw_complete_error.html')


@login_required(login_url='login')
def withdraw(request):
    if request.user.email_not_verified:
        return redirect('send_otp')


    if request.user.is_admin:
        return redirect('home_page')
    
    

    if request.POST:
        
        form = UserWithdrawRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('withdraw_complete_error')
    else:
        form = UserWithdrawRequestForm()

    context = {
            'form': form,
           
        }

    return render(request, 'account/withdraw.html', context)


@login_required(login_url='login')
def deposit(request):
    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')
        
    address = ManagerWalletAddress.objects.all()
    
    btc = ''
    eth = ''
    for address in address:
        
        btc = address.btc_wallet_address
        eth = address.eth_wallet_address
    
    if request.POST:
        
        form = UserDepositRequestForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('deposit_complete')
    else:
        form = UserDepositRequestForm()

    
    context ={
        'btc': btc,
        'eth': eth,
        'form': form,
    }
   
    
    return render(request, 'account/deposit.html', context)


@login_required(login_url='login')
def deposit_complete(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    

    if request.user.is_admin:
        return redirect('home_page')

    return render(request, 'account/deposit_complete.html')



@login_required(login_url='login')
def transaction_history(request):
    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')

    email = request.user.email
    user_deposit =  UserDepositRequest.objects.filter(email=email).order_by('-id')
    user_withdraw = UserWithdrawRequest.objects.filter(email=email).order_by('-id')

    for user in user_deposit:
        user.email
        
    context={
        'user_deposit': user_deposit,
        'user_withdraw': user_withdraw
    }
    return render(request, 'account/transaction_history.html', context)


@login_required(login_url='login')
def account_types(request):
    if request.user.email_not_verified:
        return redirect('send_otp')


    if request.user.is_admin:
        return redirect('home_page')

    level = Account_level.objects.all()

    context={
        'level': level
    }
    return render(request, 'account/account_types.html', context)


@login_required(login_url='login')
def send_otp(request):
    if request.user.is_admin:
        user = request.user
        if user.email_not_verified == True:
            user.email_not_verified = False
            user.save()
            
    if request.user.is_admin:
        return redirect('home_page')


    otp_generated = random.randint(100000,999999)
    otp_clean = str(otp_generated)

    global main_otp
    main_otp = otp_clean
    

    user_email = request.user.email
    user_first_name = request.user.first_name

    
    to = user_email
    subject = '27Cryptotrading Account Activation Code(OTP)'
    first_name = user_first_name
    message = 'Hi {0}  {1} is your activation code'.format(first_name, main_otp )
            
    
    recipient_list = [to,]    
    send_mail( subject, message, '27Cryptotrading noreply@27cryptotrading.com', recipient_list ) 
    return render(request, 'account/send_otp.html')



@login_required(login_url='login')
def send_upgrade_email(request):
    
    

    user_email = request.user.email
    

    
    to = user_email
    subject = 'Account Placed On Hold'
    
    message = render_to_string('account/upgrade_email.html')
       
    
    recipient_list = [to,]    
    send_mail( subject, message, '27Cryptotrading noreply@27cryptotrading.com', recipient_list ) 
 
    
    
   
    return render(request, 'account/send_upgrade_email.html')

@login_required(login_url='login')
def change_email_address(request):

    
    if request.POST:
        
        form = EmailAddressChangeForm(request.POST)
        if form.is_valid():
            user = request.user
            email  = form.cleaned_data.get('email')

            user.email = email
            user.save()
            messages.success(request, "Hi {} Your Email Address was changed successsfully".format(request.user.first_name))
            return redirect('send_otp')
    else:
        form = EmailAddressChangeForm()

    context = {
            'form': form
        }
            


    return render(request, 'account/change_email_address.html', context)


@login_required(login_url='login')
def validate_phone_otp(request):
    
    
    if request.POST:
        
      

        otp_o1 = request.POST['digit-1']
        otp_o2 = request.POST['digit-2']
        otp_o3 = request.POST['digit-3']
        otp_o4 = request.POST['digit-4']
        otp_o5 = request.POST['digit-5']
        otp_o6 = request.POST['digit-6']

        otp_all = otp_o1 + otp_o2 + otp_o3 + otp_o4 + otp_o5 + otp_o6
        user_otp = otp_all
        
        if user_otp == main_otp:
            
            user = request.user
            if user.email_not_verified == True:
                user.email_not_verified = False
                user.save()

            
            
            messages.success(request, "Welcome {} Your account was verified successsfully".format(request.user.first_name))
            return redirect('user_dashboard')
        else:
            messages.info(request, "Invalid OTP ")
            return redirect('validate_otp')
    return render (request, 'account/validate_otp.html', )