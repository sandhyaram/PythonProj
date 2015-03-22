
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def post(request):
	print "I am in post"
	article_post = Post.objects.all()
	art=''
	for art in Post.objects.all():
		print "Iterating through post"
		print art.title
	context ={'art': art}
	template = "post.html"	
	print "Exiting post"
	return render(request,template,context)
	

# Create your views here.

# Create your views here.
