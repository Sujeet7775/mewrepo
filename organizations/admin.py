from django.contrib import admin
from .models import Organization

# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organisation_name', 'address', 'industry_type', 'organisation_id')
    search_fields = ('organisation_name',)
    list_filter = ('industry_type',)