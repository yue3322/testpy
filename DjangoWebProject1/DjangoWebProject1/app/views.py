"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from pymongo import MongoClient
import re
import random
import urllib
from html.parser import HTMLParser
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
    collection  = db.test
    id = random.randint(10000000,99999999)
    one = collection.find_one({"id":id})
    while(collection.find_one({"id":id})): 
        id= random.randint(10000000,99999999)  
    ret = collection.insert({'id':id,'age':25,'password':pwd,'name':user})
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
    collection  = db.test
    #id = random.randint(10000000,99999999)
    list = collection.find()
   #for item in list:
     #   print(item.get("name"))
    #a = list.count()
    return render(
       request,
       'app/userlist.html',
       {
           'title':'About',
           'message':'Your application description page.',
           'list':list
       }
     )
def Crawler(request):
    rs = urllib.request.urlopen("https://www.iqshw.com/")
    html = str(rs.read())
    #pattern = re.compile('<em class="show-polution-num">*?</em>',re.S)
    result = re.search('<span id="post-date">.*:\d*</span>',html)
    #创建子类实例
    parser = MyHTMLParser()
     
    #将html数据传给解析器进行解析
    parser.feed(html)
            #替换
    phone = '18898537584 #这是我的电话号码'
    #search
    ip_addr = re.search('\d*',phone)
    return render(
            request,
            'app/Crawler.html',
            {
                
            }
        )
#定义HTMLParser的子类,用以复写HTMLParser中的方法
class MyHTMLParser(HTMLParser):
 
    #构造方法,定义data数组用来存储html中的数据
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []
 
    #覆盖starttag方法,可以进行一些打印操作
    def handle_starttag(self, tag, attrs):
        pass
        #print("Start Tag: ",tag)
        #for attr in attrs:
        #   print(attr)
     
    #覆盖endtag方法
    def handle_endtag(self, tag):
        pass
 
    #覆盖handle_data方法,用来处理获取的html数据,这里保存在data数组
    def handle_data(self, data):
        if data.count('\n') == 0:
            self.data.append(data)
 