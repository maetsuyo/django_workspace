from django.contrib import admin

# Register your models here.
from .models import Friend
from .models import Message

admin.site.register(Friend)
admin.site.register(Message)