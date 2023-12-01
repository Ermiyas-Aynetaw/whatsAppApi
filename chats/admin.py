from django.contrib import admin

# Register your models here

from chats.models import User, Chatroom, Message
admin.site.register(User)
admin.site.register(Chatroom)
admin.site.register(Message)