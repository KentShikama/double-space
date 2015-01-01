from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=128)
	poster = models.ForeignKey(User)
	content = models.TextField()
	date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.title
	def someContent(self):
		return self.content[:250] + "..."