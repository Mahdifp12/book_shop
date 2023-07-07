from django.contrib import admin
from . import models


admin.site.register(models.Book)
admin.site.register(models.BookCategory)
admin.site.register(models.BookTag)
admin.site.register(models.BookAuthor)