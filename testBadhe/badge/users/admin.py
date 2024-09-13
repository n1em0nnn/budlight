from django.contrib import admin


from .models import CustomUser





class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'compet_in')
    fieldsets = (
        (None, {
            'classes': ['wide'],
            'fields': ('username', 'password')
        }),
        ('Персональная информация', {
            'classes': ['wide'],
            'fields': ('first_name', 'last_name', 'email', 'compet_in')
        }),
        ('Права', {
            'classes': ['wide'],
            'fields': ('is_superuser', 'is_staff', 'is_active', 'groups')
        }),
        ('Даты использования', {
            'classes': ['wide'],
            'fields': ('last_login', 'date_joined')
        }),
    )
admin.site.register(CustomUser, UserAdmin)