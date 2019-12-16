from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import StoreDetail

class StoreDetailForm(ModelForm):
    class Meta:
        model = StoreDetail
        exclude = ['profile']

	
class DateInput(forms.DateInput):
	input_type = 'date'
	
	
class SearchForm(forms.Form): 
	customer_mobile_no = forms.CharField()
	start_date = forms.DateField(widget=DateInput)
	end_date = forms.DateField(widget=DateInput)