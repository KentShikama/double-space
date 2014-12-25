from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
# Create your models here.

class User(AbstractBaseUser):
    email = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    USERNAME_FIELD = 'email'
    objects = BaseUserManager()

class Category(models.Model):
	name = models.CharField(max_length=16, unique=True)
	def __str__(self):
		return self.name

class Thread(models.Model):
	title = models.CharField(max_length=128)
	poster = models.ForeignKey(User)
	image_link=models.TextField(default="http://img4.imgtn.bdimg.com/it/u=4198070164,3219625480&fm=21&gp=0.jpg")
	category = models.ForeignKey(Category)
	comment = models.TextField()
	date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.title