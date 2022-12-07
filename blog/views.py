from django.shortcuts import render

def index (request):
    return render (request, 'index.html',{})

def somos(request):
    return render (request,'somos.html',{})