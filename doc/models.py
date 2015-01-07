from django.db import models
from django.utils import timezone
import re
# Create your models here.

class Document(models.Model):
	title = models.CharField(max_length=128,blank=False,null=True,unique=True)
	content = models.TextField(default=None, blank=False, null=True)
	date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.title

from django import forms

