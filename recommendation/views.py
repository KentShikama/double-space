from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from recommendation.models import Thread,Category

# Create your views here.

def index(request):
	return render(request, 'index.html',{'threads': Thread.objects.order_by('-date')[:10]})

def post(request):
	if request.method == "GET":
		categories = Category.objects.all()
		return render(request,"post.html",{'categories':categories})
	else:
		title = request.POST['title']
		category = Category.objects.get(name = request.POST['category'])
		comment = request.POST['comment']
		image_link = request.POST['img']
		thread = Thread(poster = request.user, comment=comment, title = title, category = category)
		thread.save()
		return redirect('/')

def category(request,category_name):
	return HttpResponse("The catgories")