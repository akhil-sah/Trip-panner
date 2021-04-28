from __future__ import unicode_literals

from django.shortcuts import render,redirect
from myapp.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import *
import sqlite3
from django.contrib.auth import authenticate,login

def signup(request):
    data=Customersignup(request.GET)
    if data.is_valid():
        username = data.cleaned_data['uname']

        emailid = data.cleaned_data['email']
        e_mail = base(Email = emailid)
        e_mail.save()

        password = data.cleaned_data['psw']
        repassword = data.cleaned_data['pswrepeat']
        e = webpage(name=username, Email = e_mail,password=password,repassword=repassword)
        # request.session["name"]=e.name
        # request.session["password"]=e.password
        e.save()
        return render(request, "loggedin.html", {})

    return render(request,'register.html',{})

def contact1(request):
    data=contactus(request.GET)
    if data.is_valid():
        fullname = data.cleaned_data['fullname']

        Email = data.cleaned_data['Email']
        em = base(Email = Email)
        em.save()

        msg = data.cleaned_data['msg']

        e = contact(fullname=fullname,Email=em,msg=msg)
        # request.session["name"]=e.name
        # request.session["password"]=e.password
        e.save()
    return render(request, 'contact.html', {})
"""
def loginforms(request):
    if request.method=="GET":
        data = Loginform(request.GET)
    try:
        if data.is_valid():
            u = data.cleaned_data['uname']
            p = data.cleaned_data['psw']
            user = webpage.objects.get(name=u, password=p)

            if u == user.name and p == user.password:
                request.session["name"] = user.name
                request.session["password"] = user.password
                # return  HttpResponse("suucess..")
                # return HttpResponse("")
            # return HttpResponseRedirect("loggedin.html")
            # return HttpResponseRedirect('/prot/loggedin')

            return redirect(request, "http://127.0.0.1:8000/myapp/loggedin.html", {})

    except:
        return render(request, "loggedin.html", {})
"""
def login(request):
    if request.method == 'GET':
        try:
            form = LoginForm(request.GET)
            print(form.errors)
            if form.is_valid():
                u = form.cleaned_data['uname']
                p = form.cleaned_data['psw']
                user = webpage.objects.get(name=u, password=p)

                if u == user.name and p == user.password:
                    request.session["name"] = user.name
                    request.session["password"] = user.password
                    return render(request, "loggedin.html", {})
                else:
                    form = LoginForm()
                    return render(request, "loggedin.html", {})
        except:
            return render(request,'invalidlogin.html',{})
    else:
        form = LoginForm()
    return render(request,'login.html',{})

"""
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'], password = cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request, "loggedin.html", {})

                else:
                    return HttpResponse("Disabled Account")
"""

def logout(request):
    try:
      del request.session["name"]


    except:
        pass
    return redirect('/myapp/login/')

def payments(request):
    if request.method == 'POST':  # first try for post
        try:
            form = pay(request.POST)
            if form.is_valid():
                pck_id = form.cleaned_data['pck_id']
                obj = package.objects.get(pck_id = pck_id)
                if obj.pck_id == pck_id:
                    Email = form.cleaned_data['email']
                    em = base(Email = Email)
                    em.save()

                    name = form.cleaned_data['name']
                    card_num = form.cleaned_data['card_num']
                    month = form.cleaned_data['month']
                    year = form.cleaned_data['year']
                    cvv = form.cleaned_data['cvv']
                    pck_id = form.cleaned_data['pck_id']
    
                    e = payment(pck_id = pck_id, email = em, name = name, card_num = card_num, month = month, year = year, cvv = cvv)
                    print('lev1.5')
                    e.save()
                    print('lev2')
                    return render(request, "payment_done.html", {})
        except:
            return render(request,'wrong_pckid.html',{})
    else:
        form = pay()
    return render(request,'payment.html',{})    
    
