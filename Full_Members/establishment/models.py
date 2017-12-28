from django.db import models
from django.urls import reverse

# Create your models here.
class establishment(models.Model):

    HOTEL = 'Hotel'
    SPA = 'SPA'
    RESORT = 'Resort'
    GOLF = 'Golf Clube'
    COUNTRY = 'Country Club'
    MULTI = 'Multi Service'
    E_Types = ( (HOTEL, 'Hotel'), (SPA, 'SPA'), (RESORT, 'Resort'),(GOLF, 'Golf Clube'),
               (COUNTRY, 'Country Club'), (MULTI, 'Multi Service') )

    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE ='5'
    SIX = '6'
    SEVEN = '7'

    StarsCount = ( (ONE, '1'), (TWO, '2'), (THREE, '3'), (FOUR, '4'), (FIVE,'5'), (SIX, '6'), (SEVEN, '7') )

    Name = models.CharField(max_length = 32, unique= True)
    Establishment_type = models.CharField (max_length= 13, choices = E_Types)
    Stars = models.CharField (max_length = 1, choices = StarsCount)
    Adress = models.CharField(max_length = 128)
    Phone = models.CharField(max_length = 13)
    Web_Adress = models.URLField (max_length = 32, null= True)
    Email = models.EmailField (max_length = 36)
    Main_Photo = models.ImageField (upload_to = 'company_images', null =True)
    About = models.TextField (max_length=256, null = True )
    Logo = models.ImageField (upload_to = 'logos', null = True)

    def get_absolute_url(self):
        return reverse('establishment:Single',kwargs={'pk':self.pk})


    def __str__ (self):
        return self.Name
