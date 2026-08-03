from django.contrib import admin
from .models import Category, Project


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ['name', 'slug', 'order']
    list_editable       = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display   = ['title', 'category', 'status', 'is_featured', 'is_published']
    list_editable  = ['status', 'is_featured', 'is_published']
    list_filter    = ['status', 'category', 'is_featured', 'is_published']
    search_fields  = ['title', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Project Info', {
            'fields': (
                'title', 'slug', 'category', 'summary',
                'description', 'image', 'location'
            )
        }),
        ('Details', {
            'fields': (
                'status', 'beneficiaries',
                'start_date', 'end_date'
            )
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_published', 'meta_description'),
        }),
    )