from django.contrib import admin

from .models import *

from django.contrib.auth.admin import UserAdmin

# Register your models here.

class incomingLetters(admin.ModelAdmin):
    list_display = ('referenceNumber','subject', 'dateWritten','dateReceived','signatore',
                    'receivedFrom','cc', 'project', 'type','file','forwardedTo')
    search_fields = ('subject','referenceNumber', 'dateWritten','dateReceived','signatore',
                    'receivedFrom','cc',  'project', 'type','file','forwardedTo')
    readonly_fields = ('author', 'dateAdded','lastEdit')

    list_display_links=[
        'subject',
        'referenceNumber'
    ]

    filter_horizontal = ()
    list_filter = ("pageNumber","lastEdit")
    fieldsets = ()


class incomingMemos(admin.ModelAdmin):

    list_display = ('subject','dateWritten','signatore','receivedFrom','cc',
                    'project','pageNumber','dateAdded','file','directorate',)
    search_fields = ('subject', 'dateWritten','signatore',
                    'receivedFrom','cc',  'project','file','forwardedTo')
    readonly_fields = ('author', 'dateAdded','lastEdit')

    list_display_links=[
        'subject',
    ]

    filter_horizontal = ()
    list_filter = ("pageNumber","lastEdit")
    fieldsets = ()


class outgoingLetters(admin.ModelAdmin):
    list_display = ('referenceNumber','subject', 'dateWritten','dateDelivered','signatore',
                    'sentTo','cc', 'project', 'type','file','forwardedTo')
    search_fields = ('subject','referenceNumber', 'dateWritten','dateDelivered','signatore',
                    'sentTo','cc', 'project', 'type','file','forwardedTo')
    readonly_fields = ('author', 'dateAdded','lastEdit')

    list_display_links=[
        'subject',
        'referenceNumber'
    ]

    filter_horizontal = ()
    list_filter = ("subject","referenceNumber")
    fieldsets = ()


class directorsLetterMessages(admin.ModelAdmin):
    list_display = ('referenceNumber','messageTo','message','dateSent','author')
    search_fields = ('referenceNumber','messageTo','message','dateSent')
    readonly_fields = ('author','dateSent')

    list_display_links=[
        'referenceNumber'
    ]

    filter_horizontal = ()
    list_filter = ("referenceNumber","messageTo",)
    fieldsets = ()




admin.site.register(IncomingLetters, incomingLetters)
admin.site.register(OutgoingLetters,outgoingLetters)
admin.site.register(IncomingMemos, incomingMemos)
admin.site.register(OutgoingMemos)
admin.site.register(DirectorsLetterMessages,directorsLetterMessages)
admin.site.register(DirectorsLetterMessagesOut)
admin.site.register(DirectorsMemoMessages)
admin.site.register(DirectorsMemoMessagesOut)
admin.site.register(TeamLeadersLetterMessages)
admin.site.register(TeamLeadersLetterMessagesOut)
admin.site.register(TeamLeadersMemoMessagesOut)
admin.site.register(TeamLeadersMemoMessages)
