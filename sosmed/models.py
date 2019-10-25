from django.db import models
# Create your models here.

class instagram(models.Model):
	nama_depan =models.CharField(max_length=50)
	nama_belakang = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	context = models.CharField(max_length=100)

	def __str__(self):
		return "{}.{}".format(self.id,self.username)
