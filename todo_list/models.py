from django.db import models

class List(models.Model):
	completed = models.BooleanField(default=False)

	def __str__(self):
		return  str(self.completed)
		
