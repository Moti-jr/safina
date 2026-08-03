from django.contrib import admin
from .models import Page, MilestoneEvent


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display   = ['title', 'slug', 'is_published', 'updated_at']
    list_editable  = ['is_published']
    search_fields  = ['title']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'body', 'banner_image')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('is_published',)
        }),
    )


@admin.register(MilestoneEvent)
class MilestoneEventAdmin(admin.ModelAdmin):
    list_display = ['year', 'title', 'order']
    list_editable = ['order']
    ordering     = ['year']