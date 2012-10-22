# -*- coding: utf-8 -*- 
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ihave.core.models import *

def landing(request):
  return render_to_response('index.html')

def profile(request, user):
  u = User.objects.get(username=user)
  p = Person.objects.get(user = u)
  if u == request.user:
    return render_to_response('me.html',{'p':p})
  else:
    return render_to_response('profile.html',{'p':p})

def login_page(request):
  return render_to_response('login.html')

def login(request):
  usr = request.POST["user"]
  pas = request.POST["pass"]
  user = auth.authenticate(username=usr, password=pas)
  if user is not None:
    if user.is_active:
      auth.login(request, user)
      return HttpResponseRedirect("/%s"%usr)
    else:
      return render_to_response("login.html",{'message':'User is not activated'})
  else:
    return render_to_response("login.html",{'message':'Invalid username or password'})
  

def signup_page(request):
  return render_to_response('signup.html')

def signup(request):
  usr = request.POST["user"]
  pas = request.POST["pass"]
  repass = request.POST["repass"]
  eml = request.POST["email"]
  name = request.POST["name"]
  gender = request.POST["gender"]
  if(pas==repass):
    user = User.objects.create(username=usr,password=pas,email=eml)
    Profile.objects.create(name=name,gender=gender,user=user)
  else:
    return render_to_response('signup.html',{'message':'Passwords do not match'})


