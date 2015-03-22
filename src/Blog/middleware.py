class ReferMiddleware():
	def process_request(self,request):
		try:
			ref_id = request.GET.get("ref","")
		except:
			ref_id = False
		
		try:
			obj = EmailJoin.objects.get(ref_id = ref_id)

		except:
			obj = None
		if obj:
			request.session['join_id_ref'] = obj.id