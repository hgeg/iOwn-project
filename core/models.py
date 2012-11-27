# -*- coding: utf-8 -*- 
#######################################################
#
# author: Can Bülbül
# last edited: Sun Oct 21 2012, 7:41 PM
# description: ihave project mvp application.
#
#######################################################

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

#static data and constants
plans = ['Free Plan', 'Premium Plan', 'Platinium Plan']
  
class Global(models.Model):
  openings     =  models.IntegerField(default=20)
  announcement = models.TextField(blank=True)

class Person(models.Model): 
  #User information
  user      = models.ForeignKey(User)
  name      = models.CharField(max_length = 120)
  bio       = models.TextField()
  photo     = models.CharField(max_length = 100,default="placeholder.jpg")
  cover     = models.CharField(max_length = 100,default="cover.jpg")
  gender    = models.CharField(max_length = 1)
  
  #social data
  belongings    = models.ManyToManyField('Category')
  vote          = models.IntegerField(default=0);
  subscribers   = models.ManyToManyField('Person',related_name='ers')
  subscribing   = models.ManyToManyField('Person',related_name='ing')
  notifications = models.ManyToManyField('Info',related_name='ntf')
  messages      = models.ManyToManyField('Info',related_name='msg')

  #social network links
  #fbuser = models.CharField(max_length = 50)
  #twuser = models.CharField(max_length = 16)

  #profile information
  last_change  = models.DateTimeField(auto_now=True)
  join_date    = models.DateTimeField(auto_now_add=True)
  last_seen    = models.DateTimeField(auto_now_add=True)
  seen_count   = models.IntegerField(default=0)
  bought_count = models.IntegerField(default=0)
  sold_count   = models.IntegerField(default=0)
  item_count   = models.IntegerField(default=0)
  plan         = models.IntegerField(default=0)
  

  def ntfCount(self): return len(self.notifications.filter(state=0))
  def msgCount(self): return len(self.notifications.filter(state=0))
  def belongingList(self):
    value = self.belongings
    try:
      wishlist = list(value.filter(name='Wishlist'))
    except:
      wishlist = []
    return wishlist + list(value.filter(~Q(name='Wishlist')).order_by('last_change').reverse())

class Brand(models.Model):
  #Core information
  name     = models.CharField(max_length = 180,primary_key=True)
  image    = models.TextField()
  buy_link = models.TextField()

class Item(models.Model):
  #Meta information
  meta  = models.ForeignKey('brand')
  note  = models.CharField(max_length = 140,blank=True)
  photo = models.CharField(max_length = 100)
  show  = models.BooleanField(default=True)

  #social data
  comments = models.ManyToManyField('Info'); 
  vote     = models.IntegerField(default=0)

class Box(models.Model):
  item  = models.ForeignKey('Item')
  added = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
  boxes = models.ManyToManyField('Box')
  name  = models.CharField(max_length=100)
  last_change  = models.DateTimeField(auto_now=True)

class Info(models.Model):
  poster    = models.ForeignKey('Person')
  content   = models.TextField(null=False)
  date      = models.DateTimeField(auto_now_add=True)
  state     = models.IntegerField(default=0)
