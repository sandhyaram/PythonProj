from django.db import models

class EmailJoin(models.Model):
	email = models.EmailField(unique= True)
	friend = models.ForeignKey("self",related_name='referral',\
		                                     null =True,blank=True)
	ref_id =  models.CharField(max_length =120, default ='ABC')
	ip_address = models.CharField(max_length=120, default ='ABC ')
	timestamp = models.DateTimeField(auto_now_add= True, auto_now = False)
	update  = models.DateTimeField(auto_now_add= False, auto_now = True)

	def __unicode__(self):
		return "%s" %(self.email)


	