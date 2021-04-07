from django.contrib import admin
from .models import CustomerRequestModel

class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone', 'category']
    readonly_fields=['category']


admin.site.register(CustomerRequestModel, CustomerRequestAdmin)


