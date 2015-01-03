from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog.models import Article
from django.contrib.auth.models import User
from portal.models import Message

# Create your views here.

def all(request):
	articles=Article.objects.order_by('-date')[:10]
	users = User.objects.filter(is_superuser=True)
	return render(request,'all.html',{'users':users,'articles':articles})

def person(request,person):
	host=User.objects.get(username=person)
	articles=Article.objects.filter(poster=host).order_by('-date')[:10]
	users = User.objects.filter(is_superuser=True)
	return render(request,'all.html',{'users':users,'articles':articles,'singlePerson':True,'host':host})

def article(request,person,article):
	host=User.objects.get(username=person)
	articles=Article.objects.filter(id=article)
	users = User.objects.filter(is_superuser=True)
	return render(request,'all.html',{'users':users,'articles':articles,'singleArticle':True,'singlePerson':True,'host':host})

def compose(request):
	if request.method == "GET":
		return render(request,'compose.html',{'singlePerson':True,'singleArticle':True,'host':request.user})
	else:
		title = request.POST['title']
		content = request.POST['content']
		poster = request.user
		article = Article(title=title,content=content,poster=poster)
		article.save()
		message = Message(poster=request.user,app="blog/"+request.user.username,activity="wrote a new blog '"+title+"'.")
		message.save()
		return redirect('/blog/'+request.user.username)

def edit(request,person,article):
	if request.method == "GET":
		piece = Article.objects.all().get(id=article)
		return render(request,'edit.html',{'article':piece,'singlePerson':True,'singleArticle':True,'host':request.user})
	else:
		title = request.POST['title']
		content = request.POST['content']
		if request.user.username == person:
			piece = Article.objects.all().get(id=article)
			piece.title=title
			piece.content=content
			piece.save()
			message = Message(poster=request.user,app="blog/"+request.user.username+"/"+article,activity="updated the blog '"+title+"'.")
			message.save()
		return redirect('/blog/'+request.user.username)
