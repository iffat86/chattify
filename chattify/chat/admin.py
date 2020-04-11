from django.contrib import admin

# Register your models here.
from .models import Message, login_user

admin.site.register(Message)
admin.site.register(login_user)

