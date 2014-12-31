from django.db import models
import datetime
# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=128)
	date = models.DateField(default=datetime.date.today())
	def interval(self):
		today = datetime.date.today()
		days = (self.date-today).days
		return days
	def interval_ab(self):
		return abs(self.interval())
	def has_passed(self):
		return self.interval() <= 0
	def message(self):
		if self.has_passed:
			title.upper()+' has passed for '+self.interval_ab()+' days.'
		else:
			title.upper()+' is going to happen in '+self.interval_ab()+' days.'
	def __str__(self):
		return self.title

