from django.shortcuts import render

from .models import Shortener
from .forms import ShortenerForm
from django.http import HttpResponseRedirect,Http404

def home_view(request):
	template = 'home.html' # get the absolute base template's location(pathlib)
	context = {}

	# Empty form
	context['form'] = ShortenerForm()

	if request.method == 'GET':
		return render(request,template,context)

	elif request.method == 'POST':
		used_form = ShortenerForm(request.POST)
		if used_form.is_valid():
			# We save the for, so we also auto generate the short_urls
			shortened_object = used_form.save()

			new_url = request.build_absolute_uri('/') + shortened_object.short_url
			long_url = shortened_object.long_url

			context['new_url'] = new_url
			context['long_url'] = long_url

			return render(request,template,context)

		else:
			context['error'] = used_form.errors
			return render(request,template,context)

	
def redirect_shortened_url(request,shortened_url):
	try:
		a = Shortener.objects.get(short_url = shortened_url)
		a.times_followed += 1
		a.save()
		return HttpResponseRedirect(a.long_url)

	except Exception as e:
		# print(Shortener.objects.all())
		raise Http404('Page(long_url) is broken :(')