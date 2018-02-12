from django.shortcuts import render
from .models import Restaurant
# Create your views here.
def list(request):
	context = {
		'restaurants': Restaurant.objects.all(),
	}

	return render (request, 'restaurant.html', context)
 
def detail(request, y):
	context= {
		'x': Restaurant.objects.get(id=y),
		
	}

	return render (request, 'detailR.html', context)