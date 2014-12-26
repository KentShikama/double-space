from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from album.models import Picture
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as do_login
# Create your views here.

def index(request):
	pictures=Picture.objects.order_by('-date')
	return render(request,"main.html",{'pictures':pictures})

def upload(request):
	pics = request.FILES.getlist('photo')
	for pic in pics:
		picture = Picture(image=pic)
		picture.save()
	return redirect('/album/')

