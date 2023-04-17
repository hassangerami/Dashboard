from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['full_name', 'is_admin']
    list_filter = ('is_admin',)
    readonly_fields = ['last_login']

    fieldsets = [
        (None, {'fields': ('email', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')})
    ]

    add_fieldsets = [
        (None, {'fields': ('email', 'full_name', 'password')}),
    ]

    search_fields = ['full_name']
    ordering = ('email',)
    filter_horizontal = ['groups', 'user_permissions']


admin.site.register(User, UserAdmin)
