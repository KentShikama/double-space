from django.db import models
from django.utils import timezone
# Create your models here.



class Picture(models.Model):
	date = models.DateTimeField(default = timezone.now)
	image = models.ImageField(upload_to='media/photos')