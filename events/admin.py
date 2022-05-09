from django.contrib import admin
from .models import Events
# Register your models here.

@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display=["name","date","user", "id"]
    