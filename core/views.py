# -*- coding: utf-8 -*- 
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from core.models import *
import json,product


@login_required
def update_seen(request):
  try:
    user = request.user
    p = Person.objects.get(user = user.pk)
    p.save()
  except: pass
  return HttpResponse()

#helper methods
def me(request):
  user = request.user
  p = Person.objects.get(user = user.pk)
  return p

#request handler methods
def landing(request):
  if request.user.is_authenticated(): return HttpResponseRedirect('/me')
  return render_to_response('index.html')

@login_required
def profile(request, user=""):
    myUser = request.user
    me = Person.objects.get(user = myUser.pk)
    if user in ('','me'):
      return render_to_response('me.html',{'p':me,'me':me},context_instance=RequestContext(request))
    try:
      u = User.objects.get(username=user)
      p = Person.objects.get(user = u)
      if u == request.user:
        return render_to_response('me.html',{'p':p,'me':me},context_instance=RequestContext(request))
      else:
        p.seen_count += 1
        p.save()
        return render_to_response('profile.html',{'p':p,'me':me})
    except: 
      return render_to_response('404.html',{'p':user,'me':me})

@login_required
@csrf_exempt
def add_item(request,cat):
  if request.method == 'GET': return HttpResponseRedirect('/me/')
  name = request.POST['product']
  data = product.query(name.replace(' ','+'))[0]
  title = data['title'].split(' - ')[0] 
  try:
    b = Brand.objects.get(name=title)
  except:
    try:
      photo=data['images'][0]['thumbnails'][0]['link']
    except:
      photo="/files/image/no_image.jpg"
    b = Brand.objects.create(name=title,image=photo,buy_link=data['link'])
    b.save()
  
  description = data['description'] if len(data['description'])<141 else "%s..."%data['description'][:137]

  i = Item.objects.create(meta=b,note=description,photo="/files/image/no_image.jpg");
  i.save()
  
  bo = Box.objects.create(item=i)
  bo.save()

  me = Person.objects.get(user=request.user.pk)
  bl = me.belongings.get(name=cat)
  bl.boxes.add(bo)
  me.item_count +=1
  me.save()
  return HttpResponseRedirect('/me')

@login_required
@csrf_exempt
def add_category(request):
  if request.method == 'GET': return HttpResponseRedirect('/me/')
  category = request.POST['cat']
  b = Category.objects.create(name=category)
  b.save()
  me = Person.objects.get(user=request.user.pk)
  me.belongings.add(b)
  return HttpResponseRedirect('/me')

def lookup(request,q):
  result = product.query(q.replace(' ','+'))
  newdata = []
  for data in result:
    name = data['title'].split(' - ')[0] 
    description = data['description'] if len(data['description'])<150 else "%s..."%data['description'][:147]
    try:
      photo=data['images'][0]['thumbnails'][0]['link']
    except:
      photo="/files/image/100x100"
    newdata.append({ 'name':name, 'description':description, 'photo':photo})
  return HttpResponse(json.dumps(newdata),mimetype="application/json")

@csrf_exempt
def login(request):
  if request.user.is_authenticated(): return HttpResponseRedirect('/me')
  if request.method=="GET":
    try: n = request.GET['next']
    except: n = ''
    return render_to_response('login.html',{'n':n})
  usr = request.POST["user"]
  pas = request.POST["pass"]
  nxt = request.POST["next"]
  user = auth.authenticate(username=usr, password=pas)
  if user is not None:
    if user.is_active:
      auth.login(request, user)
      update_seen(request)
      return HttpResponseRedirect("%s"%nxt)
    else:
      return render_to_response("login.html",{'message':'This user is not activated'})
  else:
    return render_to_response("login.html",{'message':'Invalid username or password'})
  
@login_required
def logout(request): 
  if request.user.is_authenticated:
    auth.logout(request)
  return HttpResponseRedirect("/")


@login_required
def settings(request):
  if request.method == 'GET':
    return render_to_response('settings.html')
  return render_to_response('settings.html','Your preferences are successfully saved.')

@csrf_exempt
def signup(request):
  if request.user.is_authenticated(): return HttpResponseRedirect('/me')
  if request.method=="GET":
    return render_to_response('signup.html')
  
  usr = request.POST["user"]
  pas = request.POST["pass"]
  repass = request.POST["repass"]
  eml = request.POST["email"]
  name = request.POST["name"]
  sex = request.POST["gender"]
  if reduce(lambda x,y:x*y,map(len,(usr,pas,repass,eml,name)))==0 or sex=='n':
    return render_to_response('signup.html',{'message':'All fields are required.','email':eml,'name':name,'user':usr})
  if pas==repass:
    if len(User.objects.filter(username=usr))==0:
      if len(User.objects.filter(email=eml))==0:
        user = User.objects.create(username=usr,email=eml)
        user.set_password(pas)
        user.save()
        Person.objects.create(name=name,gender=sex,user=user)
        return render_to_response('success.html')
      else:
        return render_to_response('signup.html',{'message':'This email address exists.','email':eml,'name':name,'user':usr})
    else:
      return render_to_response('signup.html',{'message':'This username exists.','email':eml,'name':name,'user':usr})
  else:
    return render_to_response('signup.html',{'message':'Passwords do not match.','email':eml,'name':name,'user':usr})

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
  

  



