from . import models
from django.contrib.auth.models import User


def new_user_make(username,email,password):
	try:
		user=User.objects.create_user(username=username,email=email,password=password, is_superuser=False)
		user.save()
		return user

	except Exception as e:
		print(e)
		return ({'error':e})

def get_category_data():
	try:
		# pdb.set_trace()
		categories = list(models.category.objects.all().values())
		if categories:
			return categories
		return False
	except Exception as e:
		print(e)
		return False

def get_product_data():
	try:
		# pdb.set_trace()
		products = list(models.products.objects.all().values())
		if products:
			return products
		return False
	except Exception as e:
		print(e)
		return False