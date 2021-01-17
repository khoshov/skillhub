from django.contrib import admin

from courses.models import Course, Category, CourseCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class CourseCategoryInline(admin.TabularInline):
    model = CourseCategory
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseCategoryInline]
