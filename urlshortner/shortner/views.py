from django.shortcuts import render

from .models import Shortener
from .forms import ShortenerForm

def home_view(request):
	template = '' # get the absolute base template's location(pathlib)
	context = {}

	# Empty form
	context['form'] = ShortenerForm()

	if request.method == 'GET':
		return render(request,template,context)

	elif request.method == 'POST':
		used_form = ShortenerForm(request.POST)
		if used_form.is_valid():
			# We save the form/ so we also auto generate the short_urls
			shortened_object = used_form.save()

			new_url = request.build_absolute_uri('/') + shortened_object.short_url
			long_url = shortened_object.long_url

			context['new_url'] = new_path
			context['long_url'] = long_url

			return render(request,template,context)

		else:
			context['error'] = used_form.errors
			return render(request,template,context)

	
