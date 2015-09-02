from django.db import models

class Contact(models.Model):

	first_name = models.CharField(max_length=32, blank=True)
	last_name = models.CharField(max_length=32, blank=True)
	email = models.CharField(max_length=254, blank=True)
	phone = models.CharField(max_length=32, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
