
from django.http import HttpResponse
from django.shortcuts import render,redirect
from doc.models import Document
from portal.models import Message

def display(request):
	if request.method=="GET":
		docs=Document.objects.order_by('-date')
		return render(request,'display.html',{'docs':docs})
	else:
		idd = request.POST['id']
		title = request.POST['title']
		content = request.POST['content']
		a = Document.objects.get(id=idd)
		a.title=title
		a.content=content
		a.save()
		message = Message(poster=request.user,app="doc",activity="updated the document '"+title+"'.")
		message.save()
		return redirect('/doc/')

def new(request):
	if request.user.is_superuser:
		title = request.POST['title']
		content = request.POST['content']
		a=Document(title=title,content=content)
		a.save()
		message = Message(poster=request.user,app="doc",activity="created a document named '"+title+"'.")
		message.save()
	return redirect('/doc/')