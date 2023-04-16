from django.contrib import admin
from .models import Room, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'value', 'room',)
    search_fields = ('user', 'value', 'room',)
    


admin.site.register(Message,MessageAdmin)
admin.site.register(Room)
