from django.shortcuts import render,redirect
from .models import Restaurant, Item, Favourite
from .forms import RestaurantForm, ItemForm
from django.http import JsonResponse

# Create your views here.
def list(request):
	context = {
		'restaurants': Restaurant.objects.all(),
	}
	return render (request, 'restaurant.html', context)
 
def detail(request, y):
	restaurant_object = Restaurant.objects.get(id=y)
	items = Item.objects.filter(restaurant=restaurant_object)

	favourite_rest=[]
	favourites=request.user.favourite_set.all()
	for favourite in favourites:
		favourite_rest.append(favourite.restaurant)
	context= {
		'x': restaurant_object,
		'items': items,
		'favourite_rest':favourite_rest
		
	}
	return render (request, 'detailR.html', context)

def create(request):
	form = RestaurantForm() # we are briniging the form
	if request.method == "POST":
		form = RestaurantForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
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
			return redirect("restaurant_list")
	context = {
		"update_form" : form, # the name we want to put in our html file between {{}} hathi el bn76ha bk HTML 3shan yfham inna bnnadi el hathol el ashya2
		"obj" : restaurant_object
	}
	return render (request, 'update_form.html', context)

def delete(request, restaurant_id):
	Restaurant.objects.get(id= restaurant_id).delete()
	return redirect("restaurant_list")


def create_item(request, restaurant_id):
	restaurant_object = Restaurant.objects.get(id=restaurant_id)
	form = ItemForm() # we are briniging the form
	if request.method == "POST":
		form = ItemForm(request.POST, request.FILES or None)
		if form.is_valid():
			item = form.save(commit=False)
			item.restaurant = restaurant_object
			item.save()
			return redirect("restaurant_list")
	context = {
			'item_form': form,
			"obj" : restaurant_object
		}
	return render (request, 'Item_form.html', context)

def favourite(request, x_id):
	restaurant_obj = Restaurant.objects.get(id=x_id)
	favourite_obj, created = Favourite.objects.get_or_create(user=request.user, restaurant=restaurant_obj)
	if created:
		action="favourite"
	else:
		action="unfavourite"
		favourite_obj.delete()

	favourite_count= restaurant_obj.favourite_set.all().count()

	context = {
		'action':action,
		'count': favourite_count
	}
	return JsonResponse(context, safe=False)




