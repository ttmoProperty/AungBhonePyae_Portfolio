from django.shortcuts import render
from .models import Event, Image 

def index(request):
	context = {
		'events' : Event.objects.all(),
		'images' : Image.objects.all()
	}
	return render(request, 'application/index.html', context)