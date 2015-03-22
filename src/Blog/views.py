from django.shortcuts import render
from django.http import HttpResponse
def home(request):
	#form = emailform()
	context ={}
	template = "home.html"	
	return render(request,template,context)