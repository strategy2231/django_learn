# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food,Comment,CommentForm
from django.http import HttpResponse, HttpResponseRedirect 
import datetime 
from django.contrib.sessions.models import Session

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

def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number',8)
    return response
  
def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.') 

        
def use_session(request):
    request.session['lucky_number'] = 8                               # 設置lucky_number

    if 'lucky_number' in request.session:
        lucky_number = request.session['lucky_number']                # 讀取lucky_number

        response = HttpResponse('Your lucky_number is '+str(lucky_number))
    del request.session['lucky_number']                               # 刪除lucky_number

    return response
    
def session_test(request):
    sid = request.COOKIES['sessionid']
    sid2 = request.session.session_key
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + '<br>SessionID2:' + sid2 + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)
    
def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    request.session['restaurants'] = restaurants  # 試著利用session保存模型物件

    return render_to_response('restaurants_list.html',locals())
    