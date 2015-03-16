from django.contrib import admin
from .models import State


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(State, AuthorAdmin)
