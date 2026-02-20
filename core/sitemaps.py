from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'
    i18n = True

    def items(self):
        return ['core:home', 'core:service_list', 'core:precaution', 'core:funeral_speeches', 'core:farewell', 'core:contact']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        from django.utils import timezone
        return timezone.now()
