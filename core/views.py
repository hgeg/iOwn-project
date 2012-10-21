# -*- coding: utf-8 -*- 
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

def landing(request):
  return render_to_response('index.html')

def profile(request, user):
  return render_to_response('profile.html')
