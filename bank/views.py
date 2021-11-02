# Page Redirect , Request Page , Response Page
from django.shortcuts import render, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# Create account
from django.contrib.auth.models import User, auth
# import Tables
from .models import *
# Login account
from django.contrib.auth import authenticate, login, logout
# Gmail Request Add
import smtplib
# CSRF Token
from django.views.decorators.csrf import csrf_exempt
# Date Time
from django.utils.timezone import datetime
from datetime import date


def home(request):
    y = Blood_Donor.objects.all()
    x = len(y)
    a = Blood_Donor.objects.filter(blood_group="A+")
    a = len(a)
    a2 = Blood_Donor.objects.filter(blood_group="A-")
    a2 = len(a2)
    b = Blood_Donor.objects.filter(blood_group="B+")
    b = len(b)
    b2 = Blood_Donor.objects.filter(blood_group="B-")
    b2 = len(b2)
    ab = Blood_Donor.objects.filter(blood_group="AB+")
    ab = len(ab)
    ab2 = Blood_Donor.objects.filter(blood_group="AB-")
    ab2 = len(ab2)
    o = Blood_Donor.objects.filter(blood_group="O+")
    o = len(o)
    o2 = Blood_Donor.objects.filter(blood_group="O-")
    o2 = len(o2)
    return render(request, 'home.html', context={'y': y, 'x': x ,
     'a' : a,
     'a2' : a2,
     'b' : b,
     'b2' : b2,
     'ab' : ab,
     'ab2' : ab2,
     'o' : o,
     'o2' : o2,
    })


def addBlood(request):
    if request.method == "POST":
        name = request.POST['donor_name']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        qty = request.POST['qty']
        email = request.POST['email']
        mobile = request.POST['mobile']

        blood_donor = Blood_Donor.objects.create(
            name=name, gender=gender, blood_group=blood_group, qty=qty, email=email, mobile=mobile)
        blood_donor.save()
        return redirect('/addBlood')

    return render(request, 'addBlood.html')

def delDonor(request , id):
    a = Blood_Donor.objects.get(id=id)
    a.delete()
    return redirect("/")

def handleLogout(request):
    logout(request)
    return redirect('/')