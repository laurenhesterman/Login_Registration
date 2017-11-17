# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages



def index(request):
    return render(request, "people/index.html")


def create(request):
    result = User.objects.my_validation(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')        
    request.session['user_id'] = result.id
    messages.success(request, "Successfully Registered")
    return redirect('/success')

def login(request):
    result = User.objects.my_validation_2(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    
    request.session['user_id'] = result.id
    messages.success(request, "Thanks for logging in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "people/success.html", context)

def logout(request):
    request.session.clear()
    return render(request, "people/index.html")