from django.contrib import admin
from . import models


# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'is_active']
    list_editable = ['parent', 'is_active']


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
