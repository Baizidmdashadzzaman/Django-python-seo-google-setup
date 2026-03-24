from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from . import ai_views
from . import souvenir_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap as sitemap_xml
from accounts.sitemaps import (
    StaticViewSitemap, TourSitemap, BlogPostSitemap, 
    PageSitemap, CategorySitemap, CitySitemap, 
    CountrySitemap, DestinationRegionSitemap
)

sitemaps = {
    'static': StaticViewSitemap,
    'tours': TourSitemap,
    'blogs': BlogPostSitemap,
    'pages': PageSitemap,
    'categories': CategorySitemap,
    'cities': CitySitemap,
    'countries': CountrySitemap,
    'regions': DestinationRegionSitemap,
}

urlpatterns = [
    path('sitemap/', views.sitemap, name='sitemap'),
    path('sitemap.xml', sitemap_xml, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]
