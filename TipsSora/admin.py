from django.contrib import admin
from .models import Tips

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tips, AuthorAdmin)