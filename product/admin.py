from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Book)
admin.site.register(models.BookCategory)
admin.site.register(models.BookTag)
