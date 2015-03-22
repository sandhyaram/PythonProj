from django.contrib import admin

# Register your models here.
#.models means relative import within the folder
from .models import EmailJoin

class EmailJoinAdmin(admin.ModelAdmin):
	list_display = ['email','timestamp','update','friend']
	class Meta:
		model = EmailJoin


admin.site.register(EmailJoin, EmailJoinAdmin)
