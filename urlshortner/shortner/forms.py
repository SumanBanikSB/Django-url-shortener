from django import forms
from .models import Shortener


# from the models only the long_url is a POST, and everything is GET, so the form only passes the long_url in the fields.
# with widget HTML attributes can be passed, here a BS class.

class ShortenerForm(forms.ModelForm):
	long_url = forms.URLField(widget = forms.URLInput(
		        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}

		))

	class Meta:
		models = Shortener
		fields = ('long_url',)
