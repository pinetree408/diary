from django.contrib import admin
from diary.models import Message


class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)
