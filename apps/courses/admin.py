from django.contrib import admin

from courses.models import Category, Course, CourseCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


class CourseCategoryInline(admin.TabularInline):
    model = CourseCategory
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseCategoryInline]
