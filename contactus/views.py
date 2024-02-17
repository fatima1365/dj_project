from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from . forms import UserRegisterForm,UserLoginForm,ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'contactus/contactuspage.html')
#------------REGISTER
def user_reg(request):
    if request.method == 'POST':
        from_register = UserRegisterForm(request.POST)
        if from_register.is_valid():
            data=from_register.cleaned_data
            User.objects.create_user(username=data['username'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     email=data['email'],
                                     password=data['password'])
            return redirect('home:home-func')
    else:
        from_register=UserRegisterForm()
    context={'from_register':from_register}
    return render(request,'contactus/user_reg.html',context)

#----------LOGIN

def user_login(request):
    if request.method == 'POST':
        form_login = UserLoginForm(request.POST)
        if form_login.is_valid():
            data=form_login.cleaned_data
            user=authenticate(request,username=data['user'],
                              password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('home:home-func')
    else:
        form_login=UserLoginForm()
    return render(request,'contactus/log.html',{'form_login':form_login})

#--------------------LOGOUT
def user_logout(request):
    logout(request)
    return redirect('home:home-func')

#--------------------CHANGEPASS
@login_required()
def change_password(request):
    if request.method == 'POST':
        user=request.user
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            old_password=data['old_password']
            new_password=data['new_password']
            verify_new_password=data['verify_new_password']
            if not user.check_password(old_password):
                return HttpResponse('پسورد قبلی را درست وارد نکردید ')
            elif new_password!=verify_new_password:
                return HttpResponse('پسوردهای وارد شده مغایرت دارند')
            else:
                user.set_password(new_password)
                login(request,user)
                user.save()
                return HttpResponse('تغییرات با موفقیت اعمال شد')
    else:
        form=ChangePasswordForm()
    return render(request,'contactus/changpass.html',{'form':form})

