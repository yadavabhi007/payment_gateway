from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group



# admin.site.unregister(Group)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount', 'status', 'created_at', 'updated_at']
    search_fields = ('name', 'amount', 'status', 'created_at', 'updated_at')
    ordering = ('id', 'name', 'amount', 'status', 'created_at', 'updated_at')
    list_per_page = 15
    filter_horizontal = ()
    list_filter = ['name', 'created_at', 'updated_at']
    readonly_fields = ('created_at', 'updated_at')
