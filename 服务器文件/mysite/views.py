from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def about(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head><title> :) </title></head>
    <body>
    <h2>G Y H</h2>
    <hr>
    <p>
    Country&nbsp&nbsp&nbsp&nbsp:&nbspChina <br/>
    University&nbsp:&nbspNCU <br/>
    Wechat&nbsp&nbsp&nbsp&nbsp&nbsp:&nbspgyhdtc
    </p>
    <hr>
    <p>
    Website will be done by : Django + Nginx + Uwsgi
    </p>
    </body>
    </html>
    '''
    return render(request, 'hello.html')