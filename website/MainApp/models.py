from django.db import models
from django.contrib.auth.models import User
from . import managers

# Create your models here.
class login(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	studentid = models.CharField(max_length=100)
	creation_date=models.DateField(auto_now=True)
	modified_date=models.DateField(auto_now=True,blank=True)
	objects = managers.Login_manager()

class Room(models.Model):
    title = models.CharField(max_length=255)
    # active = models.BooleanField(default=True,blank=True)
    creation_date=models.DateField(auto_now=True)
    modified_date=models.DateField(null=True,blank=True)
    staff_only = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id

class category(models.Model):
    name = models.CharField(max_length=100)
    creation_date=models.DateField(auto_now=True)
    modified_date=models.DateField(null=True,blank=True)

class products(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    current_quantity = models.IntegerField(default=0)
    creation_date=models.DateField(auto_now=True)
    modified_date=models.DateField(null=True,blank=True)
    objects = managers.product_manager()