from django import forms
from .models import EmailJoin

class EmailForm(forms.Form):
	email= forms.EmailField()

class EmailJoinForm(forms.ModelForm):
	class Meta:
		model = EmailJoin
		fields =["email",]
		exclude = ["timestamp","update",]

	def validate_unique(self):
		pass