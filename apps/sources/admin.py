from django.contrib import admin

from sources.models import DataSource


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    pass
