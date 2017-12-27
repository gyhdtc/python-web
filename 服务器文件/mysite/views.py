from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'home.html')
def hello(request):
    return render(request, 'hello.html')
def index(request):
    return render(request, 'index.html')
def lost(request):
    return render(request, 'lost.html')