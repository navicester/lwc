# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, Http404, HttpResponse
from django.conf import settings

from .forms import EmailForm, JoinForm
from .models import Join

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(',')[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

import uuid
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id



def share(request, ref_id):

    # try:
		# join_obj = Join.objects.get(ref_id=ref_id)
		# #Exception Type: 	DoesNotExist
		# #Exception Value: 	Join matching query does not exist.
		
		# #join_obj = Join.objects.filter(ref_id=ref_id)[0]
		
		# # htmlcontent = "<html>"
		# # for instance in join_obj:
		# #     htmlcontent += "%s" % (instance)
		# # htmlcontent += "</html>"
		# # return HttpResponse(htmlcontent)
    # except:
	    # raise Http404

    # friends_referred = Join.objects.filter(friend=join_obj)
    # count = join_obj.referral.all().count()
    # #Exception Value: 	'QuerySet' object has no attribute 'referral'
    # #count = friends_referred.all().count()
    # ref_url = settings.SHARE_URL + str(join_obj.ref_id)

    # context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
    # template = "share.html"
    # return render(request, template, context)	
	
    try:
        join_obj = Join.objects.get(ref_id=ref_id)
        friends_referred = Join.objects.filter(friend=join_obj)
        count = join_obj.referral.all().count()
        ref_url = settings.SHARE_URL + str(join_obj.ref_id)

        context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
        template = "share.html"
        return render(request, template, context)
    except:
        raise Http404
def home(request):
	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
	except:
		obj = None	
	'''
	form = EmailForm(request.POST or None)
	if form.is_valid():
		email =  form.cleaned_data['email']
		new_join, created = Joins.objects.get_or_create(email=email)
		print new_join, created
	'''

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email = email)
		if created:
			new_join_old.ref_id = get_ref_id()
			if not obj == None:
				new_join_old.friend = obj
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)


# from django.template import RequestContext 
# from django.shortcuts import render_to_response 

# def server_error(request,template_name='404.html'):     
# 	return render_to_response(template_name, context_instance=RequestContext(request))