from django.contrib import admin
from . import models

class ContactAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'name','family_name','email']
    list_editable = ['email']

admin.site.register(models.ContactUs, ContactAdmin)


# Register your models here.
