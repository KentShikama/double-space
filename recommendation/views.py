from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,"index.html")

def thread(request,thread_id):
	return HttpResponse("the thread")

def category(request,category_name):
	return HttpResponse("The catgories")