from django.contrib.sitemaps import Sitemap

from core.models import MainPageConfig
from courses.models import Category


class IndexSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return MainPageConfig.objects.all()

    def lastmod(self, obj):
        return obj.updated


class CourseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.80

    def items(self):
        return Category.objects.filter()

    def lastmod(self, obj):
        return obj.updated
