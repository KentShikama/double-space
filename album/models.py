from django.db import models
from django.utils import timezone
# Create your models here.



class Picture(models.Model):
	date = models.DateTimeField(default = timezone.now)
	image = models.ImageField(upload_to='album/static/')
	def title(self):
		url = self.image.url
		parts=url.split('/')
		return parts[2]
	def __str__(self):
		return self.title()
