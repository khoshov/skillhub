from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin

from core.admin import activate, deactivate, make_draft, make_public
from courses.models import Category, CategoryAlias, Course, CourseCategory


class CategoryResource(resources.ModelResource):
    parent = fields.Field(
        column_name='parent',
        attribute='parent',
        widget=ForeignKeyWidget(Category, 'pk'),
    )

    class Meta:
        model = Category
        fields = (
            'id',
            'parent',
            'name',
            'slug',
            'description',
            'is_active',
            'sort_order',
        )


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, DraggableMPTTAdmin):
    resource_class = CategoryResource
    list_display = ('tree_actions', 'indented_title', 'slug', 'is_active', 'sort_order')
    list_filter = ('is_active',)
    prepopulated_fields = {
        'slug': ('name',)
    }
    actions = [activate, deactivate]


class CourseCategoryInline(admin.TabularInline):
    model = CourseCategory
    extra = 1


@admin.register(CategoryAlias)
class CategoryAliasAdmin(admin.ModelAdmin):
    pass


class CourseResource(resources.ModelResource):

    class Meta:
        model = Course
        exclude = ('author',)


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    list_display = ('id', 'name', 'school', 'url', 'status', 'author', 'government_support', 'created', 'updated')
    list_filter = ('categories', 'school', 'status', 'author', 'government_support')
    search_fields = ('name', 'url')
    inlines = [CourseCategoryInline]
    readonly_fields = ['author']
    actions = [make_public, make_draft]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
