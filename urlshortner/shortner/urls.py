from django.urls import path
from .views import home_view,redirect_shortened_url

urlpatterns = [
	path('',home_view,name = 'home'),
	path('<str:shortened_url>', redirect_shortened_url,name = 'redirect'),
]