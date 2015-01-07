from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Category(models.Model):
	name = models.CharField(max_length=16, unique=True)
	def __str__(self):
		return self.name

class Thread(models.Model):
	title = models.CharField(max_length=128,blank=False)
	poster = models.ForeignKey(User)
	image_link=models.TextField(default=None, blank=True, null=True)
	detail_link=models.TextField(default=None, blank=True, null=True)
	video_link=models.TextField(default=None,blank=True,null=True)
	category = models.ForeignKey(Category)
	comment = models.TextField()
	date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.title
