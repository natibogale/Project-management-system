from django.contrib import admin
from .models import (Projects,OtherProjectAttributes,ProjectMessages)
from django.contrib.auth.admin import UserAdmin

class projects(admin.ModelAdmin):
    list_display = ('projectName','contractorName','consultantName','contractType',
'location_region','startPointDistancefromAA','projectLength','directorate','assignedTo',)
    search_fields = ('subject','referenceNumber', 'dateWritten','dateReceived','signatore',
                    'receivedFrom','cc',  'project', 'type','file','forwardedTo')
    readonly_fields = ('dateAdded','author','directorate','lastEdit')

    list_display_links=[
        'projectName',
        'contractorName'
    ]

    filter_horizontal = ()
    list_filter = ("dateAdded","author")
    fieldsets = ()

class projectmessages(admin.ModelAdmin):
    list_display = ('project','message','dateSent','author')
    search_fields = ('project','message','dateSent','author')
    readonly_fields = ('author', 'dateSent')

    list_display_links=[
        'project',
        'message'
    ]

    filter_horizontal = ()
    list_filter = ("dateSent","author")
    fieldsets = ()


class otherprojectattributes(admin.ModelAdmin):
    list_display = ('project','attributeName','data','dateAdded')
    search_fields = ('project','attributeName','data')
    readonly_fields = ('author', 'dateAdded')

    list_display_links=[
        'project',
        'attributeName'

    ]

    filter_horizontal = ()
    list_filter = ("dateAdded","author")
    fieldsets = ()



admin.site.register(Projects,projects)
admin.site.register(ProjectMessages,projectmessages)
admin.site.register(OtherProjectAttributes,otherprojectattributes)


# Register your models here.
