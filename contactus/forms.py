from django import forms
from django.contrib.auth.models import User

#-----------------------REGISTER
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'insert username','class':'form'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'insert Email address','class':'form'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'insert first name','class':'form'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'insert last name','class':'form'}))
    password = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'insert password','class':'form'}))
    verify_password = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'repeat password','class':'form'}))
    age = forms.IntegerField(max_value=100,min_value=18,widget=forms.TextInput(attrs={'placeholder':'insert your age','class':'form'}))

    def clean_username(self):
        user=self.cleaned_data['username']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('کاربر وجود دارد')
        return user

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('ایمیل تکراری است')
        return email

    def clean_verify_password(self):
        password=self.cleaned_data['password']
        verify_password=self.cleaned_data['verify_password']
        if password!=verify_password:
            raise forms.ValidationError('پسوردها باهم یکی نیست')
        elif len(verify_password)<8:
            raise forms.ValidationError('پسورد کم تر از 8 کاراکتر قابل قبول نیست')
        elif not any(i.isupper() for i in verify_password):
            raise forms.ValidationError('باید حداقل دارای یک کاراکتر با حرف بزرگ باشد')
        else:return password

    def clean_age(self):
        age = self.cleaned_data['age']
        if age<18:
            raise forms.ValidationError('کمتر از سن قانونی')
        elif age>=100:
            raise forms.ValidationError('امکان فعالیت برای شما وجود ندارد')
        return age
#------------------LOGIN
class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=200)

#------------------changepass
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    verify_new_password = forms.CharField(widget=forms.PasswordInput())

