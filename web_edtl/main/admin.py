from django.contrib import admin
from main.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm, ReadOnlyPasswordHashField
)


class MyUserAdmin(UserAdmin):
    change_user_password_template = None
    ordering = ('email',)
    search_fields = ('email',)
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active',)
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Information'), {
            "fields": (
                ('first_name', 'last_name', 'address', 'mobile', 'hashed')
            ),

        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_client', 'groups',),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    change_password_form = AdminPasswordChangeForm

    class Meta:
        model = User


admin.site.register(User, MyUserAdmin)
