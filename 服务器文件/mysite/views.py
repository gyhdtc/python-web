# -*- coding: UTF-8 -*-
import markdown
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from mysite.models import Post,Blog
#from mysite.code import randomcode
#from mysite.sendemail import sendemail
import sqlite3
# Create your views here.
# Codeput = ''
# def home(request):#查看个人主页
#     return render(request, 'home.html')
#
# def index(request):#登陆界面
#     return render(request, 'index.html')
#
# def lost(request):#功能未开发
#     return render(request, 'lost.html')
#
# def hello(request):#
#     return render(request, 'hello.html')
def simple(request):
    return render(request, 'write.html')

def blog(request):# 博客中的网页数据从数据库读取，通过每个元组唯一的ID
    TAB = Blog.objects.all()
    list = []
    for x in TAB:
        article = {'title': '', 'time': '', 'id': ''}
        article['id']    = x.id
        article['title'] = x.title
        article['time']  = x.pub_date
        list.append(article)
    list.reverse()
    return render(request, 'blog.html',{'article':list})

def about(request):# 关于我
    return render(request, 'about.html')

def weixin(request):# 微信
    return render(request, 'weixin.html')

def write(request):# 写博客
    send_message = {'gyh1': '',
                    'gyh2': '',
                    'gyh3': '',
                    'gyh4': '',
                    'message': '',
                    }
    return render(request, 'write2.html', send_message)

def save(request):# 保存
    request.encoding = 'utf-8'
    if request.method == 'GET':
        send_message = {'gyh1': '',
                        'gyh2': '',
                        'gyh3': '',
                        'gyh4': '',
                        'message': '',
                        }
        yanzheng = request.GET['yanzheng'].encode('utf-8')
        title = request.GET['title'].encode('utf-8')
        body  = request.GET['blogbody']
        pub_date = request.GET['time'].encode('utf-8')
        if title != '' and body != '' and pub_date != '' and yanzheng == '/8shit8/':
            TAB = Blog.objects.all()
            try:
                Blog.objects.get(title=title)
                send_message['gyh1'] = ''
                send_message['gyh2'] = body
                send_message['gyh3'] = pub_date
                send_message['message'] += '题目重复'
            except:
                body = markdown.markdown(body)
                Blog.objects.create(id=TAB.__len__()+1,title=title,body=body,pub_date=pub_date)
                send_message['message'] += '保存成功，blog_id = ' + str((TAB.__len__()+1))
        elif title != '' and body != '' and pub_date != '' and yanzheng != '/8shit8/':
            send_message['gyh1'] = title
            send_message['gyh2'] = body
            send_message['gyh3'] = pub_date
            send_message['message'] += '验证码错误'
        else:
            send_message['message'] += '请填写完整'
    else:
        return render(request, 'write2.html')
    return render(request, 'write2.html', send_message)

def article(request,id):# 文章
    TAB = Blog.objects.get(id=id)
    send_message = {}
    send_message['title'] = TAB.title
    send_message['body']  = TAB.body
    send_message['time']  = TAB.pub_date
    return render_to_response('article.html', {'message': send_message})

def contact(request):
    return render(request, 'contact.html')

# def logup(request):#注册+个人信息
#     request.encoding = 'utf-8'
#     global Codeput
#     if request.method == 'GET':#网页提交了数据
#         id = request.GET['id'].encode('utf-8')                      # gyh1
#         email = request.GET['email'].encode('utf-8')                # gyh2
#         password = request.GET['password'].encode('utf-8')          # gyh3
#         passwordagain = request.GET['passwordagain'].encode('utf-8')# gyh4
#         codein = request.GET['code'].encode('utf-8')
#
#         send_messgae = {'gyh1': '',
#                         'gyh2': '',
#                         'gyh3': '',
#                         'gyh4': '',
#                         'messageforid': '',
#                         'messageforemail': '',
#                         'messageforpassword': '',
#                         'messagefordone': '',
#                         'code_TorF': '',
#                         }
#         send_messgae['gyh1'] = id
#         send_messgae['gyh2'] = email
#
#         if id=='' or email=='' or password=='' or passwordagain=='':
#             if id == '':
#                 send_messgae['messageforid'] += '请填写--- 用户名'
#
#             if email == '':
#                 send_messgae['messageforemail'] += '请填写--- 邮箱'
#
#             if password == '':
#                 send_messgae['messageforpassword'] += '请填写--- 密码'
#
#             return render(request,'hello.html',send_messgae)
#
#         else:
#             try:#参数读取正常，查看数据库是否有此邮箱
#                 Post.objects.get(user_email=email)
#             except:#异常，没查询到，保存数据
#                 if password == passwordagain:#查看两次密码是否一致
#                     if codein == Codeput and Codeput != '':#比较验证码
#                         gyh = Post(user_id=id,user_email=email,user_password=password)
#                         gyh.save()
#                         send_messgae['messagefordone'] += '注册成功'
#                     else:#验证码错误
#                         send_messgae['code_TorF'] += '验证码错误'
#                 else:#两次密码不正确
#                     send_messgae['messageforpassword'] += '两次密码不一致'
#             else:#查询正常，邮箱已经存在
#                 send_messgae['messageforemail'] += '邮箱已经注册'
#                 send_messgae['gyh2'] =''
#         return render(request, 'hello.html',send_messgae)
#     else:#没有提交
#         return render(request, 'hello.html')
#
# def login(request):
#     request.encoding = 'utf-8'
#     message = ''
#     if request.method == 'POST':#网页提交了数据
#         email = request.POST['email'].encode('utf-8')
#         password = request.POST['password'].encode('utf-8')
#         message = '邮箱不存在或密码错误！'
#         try:#查询数据库
#             gyh = Post.objects.get(user_email=email)
#         except:#查询不到
#             return render(request, 'index.html',{'message':message})
#         else:#查询到了
#             if password == gyh.user_password:#密码正确
#                 return render(request, 'home.html')
#             else:#密码错误
#                 return render(request, 'index.html',{'message':message})
#     else:
#         return render(request, 'index.html',{'message':message})
#
# def code(request):
#     # 全局变量
#     global Codeput
#     request.encoding = 'utf-8'
#     id = request.GET['id'].encode('utf-8')  # gyh1
#     email = request.GET['email'].encode('utf-8')  # gyh2
#     password = request.GET['password'].encode('utf-8')  # gyh3
#     passwordagain = request.GET['passwordagain'].encode('utf-8')  # gyh4
#
#     send_messgae = {'gyh1': '',
#                     'gyh2': '',
#                     'gyh3': '',
#                     'gyh4': '',
#                     'messageforid': '',
#                     'messageforemail': '',
#                     'messageforpassword': '',
#                     'messagefordone': '',
#                     'code_TorF': '',
#                     }
#     send_messgae['gyh1'] = id
#     send_messgae['gyh2'] = email
#     send_messgae['gyh3'] = password
#     send_messgae['gyh4'] = passwordagain
#     if email == '':
#         send_messgae['messageforemail'] += '请填写---邮箱'
#         return render(request, 'hello.html',send_messgae)
#     try:
#         Post.objects.get(user_email=email)
#     except:# 没查到，邮箱不存在，可以注册
#         Codeput = randomcode()  # 获取验证码，交给去全局变量
#         if sendemail(email, Codeput) == False:  # 发送验证码
#             send_messgae['code_TorF'] += '邮件发送失败'
#             return render(request, 'hello.html',send_messgae)
#         else:
#             return render(request, 'hello.html', send_messgae)
#     else:# 查到了，邮箱存在，不能注册
#         send_messgae['gyh2'] = ''
#         send_messgae['messageforemail'] += '邮箱已存在'
#         send_messgae['code_TorF'] += '邮件发送失败'
#         return render(request, 'hello.html', send_messgae)