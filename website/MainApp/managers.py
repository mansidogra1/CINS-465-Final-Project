from django import forms
from django.db import models


class Login_manager(models.Manager):
    def create_user(self,user,studentid):
    	user = self.create(user=user,studentid=studentid)
    	return user

class product_manager(models.Manager):
    def create_product(self,name,price,quantity,current_quantity):
    	product = self.create(name=name,price=price,quantity=quantity,\
			current_quantity=current_quantity)
    	return product