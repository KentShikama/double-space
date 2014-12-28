
from django.http import HttpResponse
from django.shortcuts import render,redirect
from doc.models import Document

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
		return redirect('/doc/')

def new(request):
	title = request.POST['title']
	content = request.POST['content']
	a=Document(title=title,content=content)
	a.save()
	return redirect('/doc/')