from django.db import models

class Color(models.Model):
	hex = models.CharField(max_length=7)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.hex)
