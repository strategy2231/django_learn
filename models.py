from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)
    date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3,decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField()
    restaurant = models.ForeignKey(Restaurant)
    date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.name
        
class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant)
    
class CommentForm(forms.Form):
    user = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40, required=False, label='E-mail')
    content = forms.CharField(max_length=200, widget=forms.Textarea)