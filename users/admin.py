from django.contrib import admin

from users.models import User, Company


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "company", "is_active", "avatar")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("pk", "company_name")
