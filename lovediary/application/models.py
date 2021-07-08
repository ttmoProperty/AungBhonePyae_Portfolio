from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=255)
	text = models.TextField()

	def __str__(self):
		return self.name 

class Image(models.Model):
	image = models.ImageField(upload_to='images/%Y/%m/%d')

	