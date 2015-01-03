from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from album.models import Picture
from portal.models import Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as do_login
# Create your views here.

def index(request):
	pictures=Picture.objects.order_by('-date')
	return render(request,"main.html",{'pictures':pictures})

def upload(request):
	if request.user.is_superuser:
		pics = request.FILES.getlist('photo')
		count = len(pics)
		for pic in pics:
			picture = Picture(image=pic)
			picture.save()
		message = Message(poster=request.user,app="album",activity="uploaded "+str(count)+" photos.")
		message.save()
	return redirect('/album/')

