from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from config.sitemaps import (
    StaticViewSitemap,
    ProjectSitemap,
    NewsSitemap,
    PageSitemap,
)

sitemaps = {
    'static':   StaticViewSitemap,
    'projects': ProjectSitemap,
    'news':     NewsSitemap,
    'pages':    PageSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    # Specific apps first
    path('projects/',  include('apps.projects.urls')),
    path('gallery/',   include('apps.gallery.urls')),
    path('news/',      include('apps.news.urls')),
    path('volunteer/', include('apps.volunteers.urls')),
    path('contact/',   include('apps.contact.urls')),
    path('donate/',    include('apps.donations.urls')),

    # Pages last — contains catch-all <slug:slug>/
    path('', include('apps.pages.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error pages
handler404 = 'apps.core.views.error_404'
handler500 = 'apps.core.views.error_500'

# Admin branding
admin.site.site_header  = 'Safina Initiative'
admin.site.site_title   = 'Safina Admin'
admin.site.index_title  = 'Content Management'