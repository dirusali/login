# I create a model with the required fields, I make them all mandatory to fill and to validate the iban I enforce
# a lenth of 24 characters for that field

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    firstname = models.CharField(max_length=500, blank=False, null=False)
    lastname = models.CharField(max_length=500, blank=False,null=False)
    iban = models.CharField(max_length=500, blank=False, null=False)    
    
    def save(self, *args, **kwargs):
       try:
           if len(self.iban) == 24:
                super(Profile, self).save(*args, **kwargs)
       except Excpetion as e:
           print('please enter a valid 24 digits iban code')    
           print(e)


