from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.projects.models import Project
from apps.news.models import NewsArticle
from apps.pages.models import Page


class StaticViewSitemap(Sitemap):
    priority    = 1.0
    changefreq  = 'weekly'
    protocol    = 'https'

    def items(self):
        return [
            'pages:home',
            'pages:about',
            'pages:mission',
            'pages:vision',
            'pages:history',
            'pages:faq',
            'pages:privacy',
            'projects:list',
            'news:list',
            'gallery:gallery',
            'gallery:videos',
            'volunteers:volunteer',
            'contact:contact',
            'donations:donate',
        ]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority   = 0.8
    changefreq = 'monthly'
    protocol   = 'https'

    def items(self):
        return Project.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('projects:detail', kwargs={'slug': obj.slug})


class NewsSitemap(Sitemap):
    priority   = 0.7
    changefreq = 'weekly'
    protocol   = 'https'

    def items(self):
        return NewsArticle.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('news:detail', kwargs={'slug': obj.slug})


class PageSitemap(Sitemap):
    priority   = 0.6
    changefreq = 'monthly'
    protocol   = 'https'

    def items(self):
        return Page.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('pages:page_detail', kwargs={'slug': obj.slug})