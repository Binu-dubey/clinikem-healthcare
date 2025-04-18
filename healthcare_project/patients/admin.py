from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'user', 'contact_number')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name', 'contact_number', 'user__username')
