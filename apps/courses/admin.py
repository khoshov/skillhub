from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin

from core.admin import activate, deactivate, make_draft, make_public
from courses.models import Category, Course, CourseCategory


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


class CourseCategoryInline(admin.TabularInline):
    model = CourseCategory
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school', 'status', 'author', 'government_support', 'created', 'updated')
    list_filter = ('categories', 'school', 'status', 'author', 'government_support')
    inlines = [CourseCategoryInline]
    readonly_fields = ['author']
    actions = [make_public, make_draft]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
