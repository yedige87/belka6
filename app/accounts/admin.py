from django.contrib import admin

from accounts.models import Account


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'id', 'user_type', 'email', 'phone', 'avatar')
    list_filter = ('id', 'user_type', 'first_name', 'last_name', 'email', 'phone', 'avatar')
    search_fields = ('id', 'user_type', 'first_name', 'last_name', 'email', 'phone', 'avatar')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {"fields": ('username', 'user_type', 'first_name', 'last_name', 'email', 'phone', 'avatar', "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )


admin.site.register(Account, AccountAdmin)