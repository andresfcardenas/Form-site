from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext

from form.models import ModelContact

def home(request):
	return render_to_response('layout/home/home.html',
		{'frase': 'Bienvenido al Home'},
		context_instance = RequestContext(request))

def list(request):
	entry = ModelContact.objects.order_by('id')
	paginator = Paginator(entry, 2) # show 2 articles per page

	# Make sure page request is an int. If not, deliver first page.
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	# If page request (9999) is out of range, deliver last page of results.
	try:
		page_entries = paginator.page(page)
	except (EmptyPage, InvalidPage):
		page_entries = paginator.page(paginator.num_pages)

	return render_to_response('layout/list/list.html', {'page_entries': page_entries,
		    					'entry': entry},
								context_instance = RequestContext(request))