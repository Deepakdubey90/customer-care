from django.contrib import admin
from .models import Organization


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization, AuthorAdmin)
