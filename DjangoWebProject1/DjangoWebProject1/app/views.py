"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from pymongo import MongoClient
import random
from django.views.decorators.csrf import csrf_protect

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    data = [1,2,3,4]

    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'data':data,
            'year':datetime.now().year,
        }
    )
@csrf_protect
def newUser(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newuser.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
@csrf_protect
def getUser(request):
    assert isinstance(request,HttpRequest)
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    client = MongoClient('192.168.17.191',27017)
    db = client.test
    collection  = db.User
    id = random.randint(10000000,99999999)
    one = collection.find_one({"id":id})
    while(collection.find_one({"id":id})): 
        id= random.randint(10000000,99999999)  
    ret = collection.insert({'id':id,'age':25,'password':pwd,'username':user})
    getU = collection.find_one({"id":id})
    return render(
       request,
       'app/getuser.html',
       {
           'title':'About',
           'message':'Your application description page.',
           'getU':getU
       }
     )
def userList(request):
    assert isinstance(request,HttpRequest)
    client = MongoClient('192.168.17.191',27017)
    db = client.test
    collection  = db.User
    #id = random.randint(10000000,99999999)
    list = collection.find()
    return render(
       request,
       'app/userlist.html',
       {
           'title':'About',
           'message':'Your application description page.',
           'getU':list
       }
     )