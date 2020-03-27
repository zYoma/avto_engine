from django.contrib import admin
from .models import *

class ConfirmationCodeAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'code')
    
admin.site.register(ConfirmationCode, ConfirmationCodeAdmin)
