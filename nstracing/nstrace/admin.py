from django.contrib import admin
from .models import nstracing

@admin.register(nstracing)
class NSTAdmin(admin.ModelAdmin):
    list_display = ['Request_Type','Path','Pin','Prog','Open_Id']
