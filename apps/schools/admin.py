from django.contrib import admin

from core.admin import activate, deactivate
from schools.models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_filter = ('is_active',)
    actions = [activate, deactivate]
