from django import forms
from .models import Restaurant
from .models import Item 

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name','description', 'opening_time', 'closing_time', 'image']

		widgets = {
			"opening_time" : forms.TimeInput(attrs={"type":"time"}),
			"closing_time" : forms.TimeInput(attrs={"type":"time"})
		}


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item

		exclude = ['restaurant']

			