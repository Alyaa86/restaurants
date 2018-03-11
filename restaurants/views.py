from django.shortcuts import render,redirect
from .models import Restaurant, Item, Favourite
from .forms import RestaurantForm, ItemForm
from django.http import JsonResponse, HttpResponse
from .forms import UserRegisterForm, LoginForm
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.
def user_login(request):
	form=LoginForm()
	if request.method == "POST":
		form=LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect ("restaurant_list")

	context = {
		'login' : form,
	}
	return render (request, 'login.html', context)

def signup(request):
	form=UserRegisterForm()
	if request.method == "POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect ("restaurant_list")

	context = {
		'signup' : form,
	}
	return render (request, 'signup.html', context)

def list(request):
	if request.user.is_anonymous:
		return redirect("login")

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
	if not request.user.is_authenticated:
		return redirect("login")
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
	if not (request.user.is_staff or request.user==Restaurant.owner):
		return HttpResponse ('You cannot edit this page')

	form = RestaurantForm(instance=restaurant_object) # we disply it on the form( klmat instance ehya eli tnadi el id eli 7ddnaha foog ^^)
	if request.method == "POST":
		form = RestaurantForm(request.POST, request.FILES or None, instance = restaurant_object) # eli ben gosen ohwa el m3lomat eli da5el el form .. el form mo fa'9i
		if form.is_valid():
			form.save()
			return redirect("restaurant_list")
	context = {
		"update_form" : form, # the name we want to put in our html file between {{}} hathi el bn76ha bk HTML 3shan yfham inna bnnadi el hathol el ashya2
		"obj" : restaurant_object
	}
	return render (request, 'update_form.html', context)

def delete(request, restaurant_id):
	Restaurant.objects.get(id= restaurant_id)
	if request.user.is_staff:
		Restaurant.objects.get(id= restaurant_id).delete()
		return redirect("restaurant_list")
	else:
		return HttpResponse("You cannot delete this restaurant")


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

def log_out(request):
	logout(request)
	return redirect("login")




