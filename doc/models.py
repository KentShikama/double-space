from django.db import models
from django.utils import timezone
import re
# Create your models here.

class Document(models.Model):
	title = models.CharField(max_length=128)
	content = models.TextField(default=None, blank=True, null=True)
	date = models.DateTimeField(default = timezone.now)
