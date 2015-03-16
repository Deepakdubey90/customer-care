from django.contrib import admin
from .models import Country


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, AuthorAdmin)
