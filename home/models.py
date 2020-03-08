
# I create a model the required fields and validation
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    firstname = models.CharField(max_length=500, blank=True)
    lastname = models.CharField(max_length=500, blank=True)
    iban = models.CharField(max_length=500, blank=True)


    
    def save(self, *args, **kwargs):
       try:
           if len(self.firstname) > 0 and len(self.lastname) > 0:
               if len(self.iban) == 24:
                   super(Profile, self).save(*args, **kwargs)
               else:
                   print('please enter a valid 24 digits iban code')    
           else:
               print('please enter valid name and surname')
       except Excpetion as e:
           print(e)


