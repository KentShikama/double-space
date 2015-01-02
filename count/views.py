from django.http import HttpResponse
from django.shortcuts import render,redirect
from count.models import Event
from portal.models import Message
# Create your views here.

def timeline(request):
	if request.method == "GET":
		events = Event.objects.order_by('-date')
		past, future = [],[]
		for event in events:
			if event.has_passed():
				past.append(event)
			else:
				future.append(event)
		future.reverse()
		return render(request,'timeline.html',{'pasts':past,'futures':future})
	else:
		title = request.POST['title']
		date = request.POST['date']
		event = Event(title=title,date=date)
		event.save()
		message = Message(poster=request.user,app="count",activity="created a day counter named '"+title+"'.")
		message.save()
		return redirect('/count')
