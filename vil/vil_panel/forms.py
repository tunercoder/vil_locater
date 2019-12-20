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
	
	
	def clean(self):
		cleaned_data = super(SearchForm, self).clean()
		customer_mobile_no = cleaned_data.get('customer_mobile_no')
		start_date = cleaned_data.get('start_date')
		end_date = cleaned_data.get('end_date')
		if not customer_mobile_no and not start_date and not end_date:
			raise forms.ValidationError('You have to write something!')	