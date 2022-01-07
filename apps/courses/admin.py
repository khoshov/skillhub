from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin

from core.admin import activate, deactivate, make_draft, make_public
from courses.models import Category, CategoryAlias, Course, CourseCategory


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
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


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
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
