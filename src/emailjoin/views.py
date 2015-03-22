from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.http import HttpResponse
from .forms import EmailForm, EmailJoinForm
from .models import EmailJoin

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip =""
	return ip

import uuid
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
	try:
		id_exists = EmailJoin.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id
def index(request):
	try:
		join_id = request.session['join_id_ref']
		obj = EmailJoin.objects.get(id=join_id )
		

	except:
		obj  = None
	
	#checks validation for the fileds to have values entered
	form = EmailJoinForm(request.POST or None) 
	print "here 0"
	if form.is_valid():
		#new_join =form.save(commit =False)
		print "here 1"
		email =  form.cleaned_data['email']
		new_join_old, created = EmailJoin.objects.get_or_create(email=email)
		print "here 2"
		print new_join_old.ref_id
		if created:
			new_join_old.ref_id = get_ref_id()
			#if not obj == None:
				#new_join_old.friend = obj 
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
			#print all "friends" that joined as a result of main sharer email
			#print EmailJoin.objects.filter(friend = obj)
		else:
			print "User exists, reusing"
		if new_join_old.ref_id:
			return HttpResponseRedirect("foo%s" %(new_join_old.ref_id))

	
	context ={"form":form}
	template = "index.html"	
	return render(request,template,context)

def home(request,ref_id):
	#Count= ref_id.count("ref_id")
	print  "*********** %s" %ref_id
	for element in EmailJoin.objects.all():
		print element.ref_id
		print element.email
		if element.ref_id is ref_id:
			print "match found, hurrah! %s" %element.email
	join_obj = EmailJoin.objects.get(ref_id=ref_id)
	
	ref_url= settings.SHARE_URL + str(join_obj.ref_id)
	context = {"ref_id":join_obj.ref_id, "ref_url":ref_url}
	template = "home.html"
	return render(request,template,context)
	#return request.session.flush()
