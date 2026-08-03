from django.contrib import admin
from .models import NewsTag, NewsArticle


@admin.register(NewsTag)
class NewsTagAdmin(admin.ModelAdmin):
    list_display        = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display   = ['title', 'published_at', 'is_featured', 'is_published']
    list_editable  = ['is_featured', 'is_published']
    list_filter    = ['is_published', 'is_featured', 'tags']
    search_fields  = ['title', 'summary']
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Article', {
            'fields': (
                'title', 'slug', 'summary',
                'body', 'image', 'published_at'
            )
        }),
        ('Categorisation', {
            'fields': ('tags',)
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_published', 'meta_description')
        }),
    )