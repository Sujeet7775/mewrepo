from django.contrib import admin
from .models import ModuleMaster

# Register your models here.
@admin.register(ModuleMaster)
class ModuleMasterAdmin(admin.ModelAdmin):
    list_display = ('module_name', 'app_name', 'actions')
    search_fields = ('model_name',)
    list_filter = ('app_name',)