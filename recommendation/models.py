from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Category(models.Model):
	name = models.CharField(max_length=16, unique=True)
	def __str__(self):
		return self.name

class Thread(models.Model):
	title = models.CharField(max_length=128)
	poster = models.ForeignKey(User)
	image_link=models.TextField(default="http://ts2.mm.bing.net/th?id=HN.608014447209022679&pid=1.7")
	category = models.ForeignKey(Category)
	comment = models.TextField()
	date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.title