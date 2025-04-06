from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'location', 'available')
    list_filter = ('specialization', 'location', 'available')
    search_fields = ('name', 'specialization', 'location')
