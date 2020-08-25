from django.db import models

from .validators import validateNama

# Create your models here.



class ContactModel(models.Model):
	gend = (
			('P', 'Pria'),
			('W', 'Wanita'),
		)



	nama			= models.CharField(max_length=40, validators=[validateNama])
	gender			= models.CharField(max_length=6, choices=gend)
	tanggal_lahir	= models.DateTimeField()
	alamat			= models.TextField()
	email			= models.EmailField()

	def __str__(self):
		return "{}. {}".format(self.id, self.nama)