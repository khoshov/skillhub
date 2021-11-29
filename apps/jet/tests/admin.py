from jet.tests.models import RelatedToTestModel, TestModel

from django.contrib import admin


class TestModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')


class RelatedToTestModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(TestModel, TestModelAdmin)
admin.site.register(RelatedToTestModel, RelatedToTestModelAdmin)
