from django.contrib import admin


@admin.action(description='Установить статус опубликовано')
def make_public(modeladmin, request, queryset):
    queryset.update(status=modeladmin.model.PUBLIC)


@admin.action(description='Установить статус черновик')
def make_draft(modeladmin, request, queryset):
    queryset.update(status=modeladmin.model.DRAFT)


@admin.action(description='Установить статус активный')
def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Удалить статус активный')
def deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)
