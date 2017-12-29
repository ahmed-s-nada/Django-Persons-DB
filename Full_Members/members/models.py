from django.db import models
from django.contrib.auth.models import User
from establishment.models import establishment


# Create your models here.

class member(models.Model):
    MALE = 'Mr'
    FEMALE = 'Mrs'
    GAY = "Seco"
    GENDER_CHOICES = ( (MALE, 'Male'), (FEMALE, 'Female'), (GAY, 'Gay'))

    SINGLE = 'S'
    FAMILY = 'F'
    MEMBERSHIP_CHOICES = ( (SINGLE, 'Single'), (FAMILY, 'Family') )

    User_Name = models.CharField(max_length = 12)
    First_Name = models.CharField(max_length = 16)
    Last_Name = models.CharField(max_length = 16)
    place= models.ForeignKey(establishment, on_delete=None, default= 1)
    Gender = models.CharField(max_length = 4, choices = GENDER_CHOICES,default = MALE)
    birthDay= models.DateField(default = '07/07/1977')
    Email = models.EmailField(max_length= 128)
    Memebership_type= models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default= SINGLE)
    profile_image = models.ImageField(upload_to = 'profiles', null = True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null = True )

    def __str__ (self):
        return self.User_Name
