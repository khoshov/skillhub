from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin

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
    inlines = [CourseCategoryInline]
    readonly_fields = ['author']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
