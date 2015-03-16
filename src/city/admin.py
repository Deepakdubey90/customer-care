from django.contrib import admin
from .models import City


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(City, AuthorAdmin)
