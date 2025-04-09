from django.contrib import admin
from .models import User, ageUser_tb, educationLevelUser_tb, relationKindUser_tb, workUser_tb, rangeSalary_tb

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, AuthorAdmin)

admin.site.register(ageUser_tb, AuthorAdmin)

admin.site.register(educationLevelUser_tb, AuthorAdmin)

admin.site.register(relationKindUser_tb, AuthorAdmin)

admin.site.register(workUser_tb, AuthorAdmin)

admin.site.register(rangeSalary_tb, AuthorAdmin)
