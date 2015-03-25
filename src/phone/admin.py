from django.contrib import admin
from .models import Phone


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phone, AuthorAdmin)
