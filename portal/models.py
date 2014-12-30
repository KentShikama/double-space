from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

now = datetime.datetime.now()

# Create your models here.

class Message(models.Model):
	date = models.DateTimeField(default = now)
	poster = models.ForeignKey(User)
	app = models.CharField(max_length=128,default="")
	activity = models.TextField(default=None, blank=True, null=True)
	def sentence(self):
		return str(self.date.date())+":  " + self.poster.username + " " + self.activity
	def __str__(self):
		return self.sentence()