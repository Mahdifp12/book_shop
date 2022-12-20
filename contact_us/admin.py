from django.contrib import admin
from . import models


# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_date', 'full_name']


admin.site.register(models.ContactUs, ContactUsAdmin)
