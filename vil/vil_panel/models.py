from django.db import models
from django.utils import timezone
from users import models as users_model
from django.urls import reverse

YES_NO_CHOICES = (
   ('1', 'Yes'),
   ('0', 'No')
)

class StoreDetail(models.Model):	
    is_new_customer = models.CharField(choices=YES_NO_CHOICES, max_length=2)	
    is_postpaid = models.CharField(choices=YES_NO_CHOICES, max_length=2)
    customer_name = models.CharField('Customer Name', max_length=120, blank=True, null=True)
    customer_mobile_no = models.CharField('Contact Number', max_length=20, blank=True, null=True)
    is_4g_sim_upgrade_pitched = models.BooleanField(default=False)	
    is_4g_sim_upgrade_converted = models.BooleanField(default=False)	
    is_voda_idea_app_pitched = models.BooleanField(default=False)	
    is_voda_idea_app_converted = models.BooleanField(default=False)	
    is_non_telco_offer_edu_pitched = models.BooleanField(default=False)	
    is_non_telco_offer_edu_converted = models.BooleanField(default=False)	
    is_plan_upgrading_to_unlimited_pitched = models.BooleanField(default=False)	
    is_plan_upgrading_to_unlimited_converted = models.BooleanField(default=False)	
    is_email_updation_pitched = models.BooleanField(default=False)	
    is_email_updation_converted = models.BooleanField(default=False)	
    is_non_mobility_pitched = models.BooleanField(default=False)	
    is_non_mobility_converted = models.BooleanField(default=False)	
    is_reference_add_on_pitched = models.BooleanField(default=False)	
    is_reference_add_on_converted = models.BooleanField(default=False)	
    insertion_date_time = models.DateTimeField(auto_now_add=True,verbose_name='creation date')
    updation_date_time = models.DateTimeField(auto_now=True,verbose_name='last updated on')
    profile = models.ForeignKey(users_model.Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
	    return self.customer_name

    def get_absolute_url(self):#To let object get path and where to be routed after successful creation
	    return reverse('vilpanel-storedetail',kwargs ={'pk': self.pk})
		
    def get_fields(self):
	    return [(field.name, field.value_to_string(self)) for field in StoreDetail._meta.fields]

