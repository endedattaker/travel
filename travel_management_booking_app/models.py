from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    #Place = models.ForeignKey(Packages, on_delete=models.CASCADE) 


    def __str__(self):
        return self.name
    
class Packages(models.Model):
    Image=models.ImageField(upload_to='images')
    Place=models.CharField(max_length=900)
    Days=models.IntegerField()
    Persons=models.IntegerField()
    Price=models.IntegerField()
    Trip=models.CharField(max_length=900)
    Description=models.CharField(max_length=900)
   
    def __str__(self):
        return self.Place
    


