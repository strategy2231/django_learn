# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food,Comment,CommentForm
from django.http import HttpResponse, HttpResponseRedirect 
import datetime 
def menu(request):
    if 'id' in request.GET:
        print(type(request.GET['id']))
        r = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")
  
def meta(request):
    values = request.META.items()  # 將字典的鍵值對抽出成為一個清單

    values.sort()                  # 對清單進行排序

    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))
    
def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html',locals())
    
 
def comment(request,id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if 'ok' in request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            user = f.cleaned_data['user']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = datetime.datetime.now()
            c = Comment(user=user, email=email, content=content, date_time=date_time, restaurant=r)
            c.save()
            f = CommentForm(initial={'content':'我沒意見'})
    else:
        f = CommentForm(initial={'content':'我沒意見'})
    return render_to_response('comments.html',locals())
    
