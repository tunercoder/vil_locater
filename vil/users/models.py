from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('ST', 'Store'),
        ('SM', 'Store Manager'),
        ('CL', 'Circle'),
        ('ZN', 'Zone'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=2,choices=USER_TYPE_CHOICES)	
    store_name = models.CharField('Store Name', max_length=120, blank=True, null=True)
    contact_no = models.CharField('Contact Number', max_length=20, blank=True, null=True)
    zone_name = models.CharField('Zone Name', max_length=120, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'

