# -*- coding: utf-8 -*- 
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from core.models import *

#helper methods
def me(request):
  user = request.user
  p = Person.objects.get(user = user.pk)
  return p

#request handler methods
def landing(request):
  return render_to_response('index.html')

#@login_required
def profile(request, user=""):
    if user=="":
      #user = request.user
      #p = Person.objects.get(user = user.pk)
      p = Person.objects.all()[0]
      return render_to_response('profile.html',{'p':p,'title':"%s's profile"%(p.user.username)})

    u = User.objects.get(username=user)
    p = Person.objects.get(user = u)
    if u == request.user:
      return render_to_response('profile.html',{'p':p,'myUser':request.user.username})
    else:
      p.seen_count += 1
      p.save()
      return render_to_response('profile.html',{'p':p,'myUser':request.user.username})

def login_page(request):
  return render_to_response('login.html')

@csrf_exempt
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
  
@login_required
def logout(request): 
  if request.user.is_authenticated:
    auth.logout(request)
  return HttpResponseRedirect("/")

@login_required
def settings_page(request):
  return render_to_response('settings.html')

@login_required
def save_settings(request): pass

def signup_page(request):
  return render_to_response('signup.html')

@csrf_exempt
def signup(request):
  usr = request.POST["user"]
  pas = request.POST["pass"]
  repass = request.POST["repass"]
  eml = request.POST["email"]
  name = request.POST["name"]
  gender = request.POST["gender"]
  if pas==repass:
    if len(User.objects.filter())==0:
      if gender!="n":
        user = User.objects.create(username=usr,email=eml)
        user.set_password(pas)
        user.save()
        Person.objects.create(name=name,gender=gender,user=user)
        return HttpResponseRedirect('/me/')
      else:
        return render_to_response('signup.html',{'message':'Please select a gender.'})
    else:
      return render_to_response('signup.html',{'message':'This username exists.'})
  else:
    return render_to_response('signup.html',{'message':'Passwords do not match.'})

#push notification methods
@login_required
def updateProfileNotifications(request):
  p = me(request)
  return HttpResponse('{"n":%d,"m":%d}'%(p.ntfCount,p.msgCount),content_type="application/json")

def updateComments(request,i):
  item = Item.objects.get(id=i)
  comments = item.comments.filter(state=0).order_by("date")
  return HttpResponse(serializers.serialize('json',comments),content_type="application/json")

def updateMessages(request):
  p = me(request)
  messages = p.messages.filter(state=0).order_by("date")
  return HttpResponse(serializers.serialize('json',messages),content_type="application/json")
  

  



