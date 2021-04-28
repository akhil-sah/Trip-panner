from django import forms
from .models import package

class Customersignup(forms.Form):
    uname = forms.CharField(max_length=100)
    email=forms.EmailField(widget = forms.EmailInput)
    psw=forms.CharField(widget = forms.PasswordInput)
    pswrepeat=forms.CharField(widget = forms.PasswordInput)



class contactus(forms.Form):
    fullname = forms.CharField(max_length=100)
    Email=forms.EmailField(widget = forms.EmailInput)
    msg=forms.CharField(widget = forms.TextInput)

"""
class Loginform(forms.Form):
    uname = forms.CharField(max_length=100)
    psw = forms.CharField(widget = forms.PasswordInput)
"""
class LoginForm(forms.Form):
	uname = forms.CharField(max_length = 20)               #EmailField()
	psw = forms.CharField(widget = forms.PasswordInput)

class pay(forms.Form):
    pck_id = forms.IntegerField()  #consider case for wrong id entered
    email = forms.EmailField(widget = forms.EmailInput)
    name = forms.CharField(max_length = 30)
    card_num = forms.IntegerField()
    month = forms.CharField(max_length = 10)
    year = forms.IntegerField()
    cvv = forms.IntegerField()