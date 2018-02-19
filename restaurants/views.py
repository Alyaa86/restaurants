from django.shortcuts import render,redirect
from .models import Restaurant
from .forms import RestaurantForm

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

def create(request):
	form = RestaurantForm() # we are briniging the form
	if request.method == "POST":
		form = RestaurantForm(request.POST)
		if form.is_valid():
			form.save(),
			return redirect("restaurant_list")
	context = {
			'create_form': form
		}
	return render (request, 'restaurant_form.html', context)

def update(request,restaurant_id):
	restaurant_object = Restaurant.objects.get(id=restaurant_id) # awal shai we call the id we want to modify
	form = RestaurantForm(instance=restaurant_object) # we disply it on the form( klmat instance ehya eli tnadi el id eli 7ddnaha foog ^^)
	if request.method == "POST":
		form = RestaurantForm(request.POST, instance = restaurant_object) # eli ben gosen ohwa el m3lomat eli da5el el form .. el form mo fa'9i
		if form.is_valid():
			form.save()
	context = {
		"update_form" : form, # the name we want to put in our html file between {{}} hathi el bn76ha bk HTML 3shan yfham inna bnnadi el hathol el ashya2
		"obj" : restaurant_object
	}
	return render (request, 'update_form.html', context)

def delete(request, restaurant_id):
	Restaurant.objects.get(id= restaurant_id).delete()
	return redirect("restaurant_list")







