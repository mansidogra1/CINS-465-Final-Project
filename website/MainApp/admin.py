from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.login)
admin.site.register(models.Room)
admin.site.register(models.category)
admin.site.register(models.products)