
from django.http import HttpResponse
from django.shortcuts import render,redirect
from album.models import Picture
from portal.models import Message
# Create your views here.

def index(request):
	pictures=Picture.objects.order_by('-date')[:10]
	messages=Message.objects.order_by('-date')[:10]
	return render(request,"gate.html",{'pictures':pictures,'messages':messages})
