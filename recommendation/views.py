from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from recommendation.models import Thread,Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as do_login

# Create your views here.

def index(request):
	return render(request, 'index.html',{'threads': Thread.objects.order_by('-date'),'categories':Category.objects.all()})

def post(request):
	if request.method == "GET":
		categories = Category.objects.all()
		return render(request,"post.html",{'categories':categories})
	else:
		title = request.POST['title']
		category = Category.objects.get(name = request.POST['category'])
		comment = request.POST['comment']
		image_link = request.POST['img']
		thread = Thread(poster = request.user, comment=comment, title = title, category = category,image_link=image_link)
		thread.save()
		return redirect('/recommendation')


def login(request):
	if request.method == "GET":
		users = User.objects.all()
		return render(request,'login.html',{'users':users})
	else:
		username = request.POST['user']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user:
			do_login(request,user)
			return redirect('/recommendation')
		else:
			users = User.objects.all()
			context = {'invalid_login':True,'users':users}
			return render(request,'login.html',context)

def category(request,category_name):
	return HttpResponse("The catgories")