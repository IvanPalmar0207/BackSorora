from django.contrib import admin
from .models import AlternativeActions_tb, MediaAlternative_tb

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(AlternativeActions_tb, AuthorAdmin)
admin.site.register(MediaAlternative_tb, AuthorAdmin)