from django.contrib import admin
from .models import categoryTestimonie_tb, testimonies_tb

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(categoryTestimonie_tb, AuthorAdmin)
admin.site.register(testimonies_tb, AuthorAdmin)