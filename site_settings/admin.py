from django.contrib import admin
from . import models


# Register your models here.

class FooterLinksAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'url'
    ]


admin.site.register(models.SiteSettings)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.FooterLinks)
