# -*- coding: UTF-8 -*-
from django.shortcuts import render
from mysite.models import Post,Blog
from mysite.code import randomcode
from mysite.sendemail import sendemail

# Create your views here.
Codeput = ''
def home(request):#查看个人主页
    return render(request, 'home.html')

def index(request):#登陆界面
    return render(request, 'index.html')

def lost(request):#功能未开发
    return render(request, 'lost.html')

def hello(request):#
    return render(request, 'hello.html')

def blog(request):#
    return render(request, 'blog.html')

def about(request):#
    return render(request, 'about.html')

def contact(request):#
    return render(request, 'contact.html')

def fullwidth(request):#
    return render(request, 'full-width.html')

def single(request):#
    return render(request, 'single.html')

def write(request):#
    return render(request, 'write.html')

def article(request,id):#
    return render(request, 'write.html')

def logup(request):#注册+个人信息
    request.encoding = 'utf-8'
    global Codeput
    if request.method == 'GET':#网页提交了数据
        id = request.GET['id'].encode('utf-8')                      # gyh1
        email = request.GET['email'].encode('utf-8')                # gyh2
        password = request.GET['password'].encode('utf-8')          # gyh3
        passwordagain = request.GET['passwordagain'].encode('utf-8')# gyh4
        codein = request.GET['code'].encode('utf-8')

        send_messgae = {'gyh1': '',
                        'gyh2': '',
                        'gyh3': '',
                        'gyh4': '',
                        'messageforid': '',
                        'messageforemail': '',
                        'messageforpassword': '',
                        'messagefordone': '',
                        'code_TorF': '',
                        }
        send_messgae['gyh1'] = id
        send_messgae['gyh2'] = email

        if id=='' or email=='' or password=='' or passwordagain=='':
            if id == '':
                send_messgae['messageforid'] += '请填写--- 用户名'

            if email == '':
                send_messgae['messageforemail'] += '请填写--- 邮箱'

            if password == '':
                send_messgae['messageforpassword'] += '请填写--- 密码'

            return render(request,'hello.html',send_messgae)

        else:
            try:#参数读取正常，查看数据库是否有此邮箱
                Post.objects.get(user_email=email)
            except:#异常，没查询到，保存数据
                if password == passwordagain:#查看两次密码是否一致
                    if codein == Codeput and Codeput != '':#比较验证码
                        gyh = Post(user_id=id,user_email=email,user_password=password)
                        gyh.save()
                        send_messgae['messagefordone'] += '注册成功'
                    else:#验证码错误
                        send_messgae['code_TorF'] += '验证码错误'
                else:#两次密码不正确
                    send_messgae['messageforpassword'] += '两次密码不一致'
            else:#查询正常，邮箱已经存在
                send_messgae['messageforemail'] += '邮箱已经注册'
                send_messgae['gyh2'] =''
        return render(request, 'hello.html',send_messgae)
    else:#没有提交
        return render(request, 'hello.html')

def login(request):
    request.encoding = 'utf-8'
    message = ''
    if request.method == 'POST':#网页提交了数据
        email = request.POST['email'].encode('utf-8')
        password = request.POST['password'].encode('utf-8')
        message = '邮箱不存在或密码错误！'
        try:#查询数据库
            gyh = Post.objects.get(user_email=email)
        except:#查询不到
            return render(request, 'index.html',{'message':message})
        else:#查询到了
            if password == gyh.user_password:#密码正确
                return render(request, 'home.html')
            else:#密码错误
                return render(request, 'index.html',{'message':message})
    else:
        return render(request, 'index.html',{'message':message})

def code(request):
    # 全局变量
    global Codeput
    request.encoding = 'utf-8'
    id = request.GET['id'].encode('utf-8')  # gyh1
    email = request.GET['email'].encode('utf-8')  # gyh2
    password = request.GET['password'].encode('utf-8')  # gyh3
    passwordagain = request.GET['passwordagain'].encode('utf-8')  # gyh4

    send_messgae = {'gyh1': '',
                    'gyh2': '',
                    'gyh3': '',
                    'gyh4': '',
                    'messageforid': '',
                    'messageforemail': '',
                    'messageforpassword': '',
                    'messagefordone': '',
                    'code_TorF': '',
                    }
    send_messgae['gyh1'] = id
    send_messgae['gyh2'] = email
    send_messgae['gyh3'] = password
    send_messgae['gyh4'] = passwordagain
    if email == '':
        send_messgae['messageforemail'] += '请填写---邮箱'
        return render(request, 'hello.html',send_messgae)
    try:
        Post.objects.get(user_email=email)
    except:# 没查到，邮箱不存在，可以注册
        Codeput = randomcode()  # 获取验证码，交给去全局变量
        if sendemail(email, Codeput) == False:  # 发送验证码
            send_messgae['code_TorF'] += '邮件发送失败'
            return render(request, 'hello.html',send_messgae)
        else:
            return render(request, 'hello.html', send_messgae)
    else:# 查到了，邮箱存在，不能注册
        send_messgae['gyh2'] = ''
        send_messgae['messageforemail'] += '邮箱已存在'
        send_messgae['code_TorF'] += '邮件发送失败'
        return render(request, 'hello.html', send_messgae)