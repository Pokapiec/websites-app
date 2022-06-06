from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Website)
admin.site.register(models.WebPage)
admin.site.register(models.WebsiteCategory)
