from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=250, unique= True)
	date_added = models.DateTimeField(default= "")
	image = models.TextField(max_length=1000,null=True, blank=True)
	tags = models.TextField(max_length=500,null=True,blank=True)
	article = models.TextField(max_length=15000,null =True, blank= True)
	author = models.CharField(max_length=150,null=True,blank=True)

	def get_absolute_url(self):
		return "%s" %(self.title)

# Create your models here.


# Create your models here.
