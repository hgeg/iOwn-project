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

#static data and constants
plans = ['Free Plan', 'Premium Plan', 'Platinium Plan']

class Person(models.Model): 
  #User information
  user      = models.ForeignKey(User)
  name      = models.CharField(max_length = 120)
  bio       = models.TextField()
  photo     = models.CharField(max_length = 100,default="/files/img/default_avatar.jpg")
  cover     = models.CharField(max_length = 100,default="/files/img/default_cover.jpg")
  gender    = models.CharField(max_length = 1)
  
  #social data
  boxes         = models.ManyToManyField('Box')
  vote          = models.IntegerField(default=0);
  subscribers   = models.ManyToManyField('Person',related_name='ers')
  subscribing   = models.ManyToManyField('Person',related_name='ing')
  notifications = models.ManyToManyField('Info',related_name='ntf')
  messages = models.ManyToManyField('Info',related_name='msg')

  #profile information
  last_change = models.DateTimeField(auto_now_add=True)
  seen_count  = models.IntegerField(default=0)
  join_date   = models.DateTimeField(auto_now=True)
  plan        = models.IntegerField(default=0)

  def ntfCount(self): return len(self.notifications.filter(state=0))
  def msgCount(self): return len(self.notifications.filter(state=0))

class Brand(models.Model):
  #Core information
  name  = models.CharField(max_length = 120,primary_key=True)
  photo = models.CharField(max_length = 100)
  buy_link = models.URLField(blank=True)

class Item(models.Model):
  #Meta information
  meta = models.ForeignKey('brand')
  note  = models.CharField(max_length = 140,blank=True)
  photo = models.CharField(max_length = 100)

  #social data
  comments = models.ManyToManyField('Info'); 
  vote     = models.IntegerField(default=0)

class Box(models.Model):
  xpos = models.IntegerField()
  ypos = models.IntegerField()

  rows = models.IntegerField(default=2)
  cols = models.IntegerField(default=2)
  
  boxes = models.ManyToManyField('BoxItem') 
  
class BoxItem(models.Model):
  index = models.IntegerField()
  item  = models.ForeignKey('Item')

class Info(models.Model):
  poster    = models.ForeignKey('Person')
  content   = models.TextField(null=False)
  date      = models.DateTimeField(auto_now_add=True)
  state     = models.IntegerField(default=0)
