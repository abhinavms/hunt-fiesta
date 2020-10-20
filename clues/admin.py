from django.contrib import admin
from .models import Level
# Register your models here.

class LevelAdmin(admin.ModelAdmin):
    model = Level
    list_display = ('no', 'text', 'picture', 'hiddenHTML', 'answer')
    # fieldsets = (
    #     (None, {'fields': ('email', 'password', 'level')}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
    #     ),
    # )
    search_fields = ('no',)
    ordering = ('no',)

admin.site.register(Level, LevelAdmin)