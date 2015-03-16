from django.contrib import admin
from .models import Office


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Office, AuthorAdmin)
