from django.contrib import admin
from .models import (User, Teams, Directorates)
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class listAdmin(UserAdmin):
    list_display = ('admin_photo','username', 'firstName','middleName','lastName',
                    'email','directorate', 'team', 'title', 'is_admin')
    search_fields = ('username', 'firstName','middleName','lastName',
                    'email','directorate', 'team', 'title')
    readonly_fields = ('admin_photo','date_joined', 'last_login','lastEdit')
    
    list_display_links=[
        'username',
        'admin_photo'
    ]
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(User, listAdmin)
admin.site.register(Teams)
admin.site.register(Directorates)