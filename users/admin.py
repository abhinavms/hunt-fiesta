from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Logs

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'level', 'is_staff', 'is_active')
    list_filter = ('level', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'level')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class LogsAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('user', 'level', 'text', 'ip_address', 'datetime')
    list_filter = ('user', 'level', 'ip_address', 'datetime')
    
    ordering = ('datetime',)

admin.site.register(Logs, LogsAdmin)