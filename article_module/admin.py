from django.contrib import admin
from django.http import HttpRequest

from . import models
from .models import Article


# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'parent',
        'is_active',
    ]
    list_editable = [
        'parent',
        'is_active'
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        'slug',
        'author'
    ]
    list_editable = [
        'is_active',
        'slug'
    ]

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user

        return super().save_model(request, obj, form, change)


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ArticleComment)
