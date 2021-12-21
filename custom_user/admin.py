from django.contrib import admin
from . import models
# Register your models here.
from custom_user.models import CustomUser

admin.site.register(models.CustomUser)