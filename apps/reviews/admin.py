from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from reviews.models import Review


class ReviewResource(resources.ModelResource):

    class Meta:
        model = Review


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('id', 'url', 'rating', 'school', 'source', 'published')
    list_filter = ('school', 'rating', 'source', 'published')
    resource_class = ReviewResource
