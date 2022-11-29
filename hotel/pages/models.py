from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    Mob_no=models.CharField(max_length=15)
    textmsg= models.CharField(max_length=200)

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.IntegerField()
    
