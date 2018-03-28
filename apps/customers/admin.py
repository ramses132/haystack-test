from django.contrib import admin
from .models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid_until', 'on_trial', 'created', 'modified')

admin.site.register(Client, ClientAdmin)
