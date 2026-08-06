from django.contrib import admin
from .models import SiteSettings, HeroSlide, Statistic, Testimonial, TeamMember, FAQ


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General', {
            'fields': ('site_name', 'tagline', 'logo', 'favicon')
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'address')
        }),
        ('Social Media', {
            'fields': ('facebook', 'twitter', 'instagram', 'youtube')
        }),
        ('Footer', {
            'fields': ('footer_text',)
        }),
    )

    def has_add_permission(self, request):
        # Only one settings row allowed
        return not SiteSettings.objects.exists()


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display  = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering      = ['order']


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display  = ['label', 'value', 'icon', 'order', 'is_active']
    list_editable = ['value', 'order', 'is_active']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display  = ['name', 'role', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter   = ['is_active']
    search_fields = ['name', 'role']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display  = ['name', 'role', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'role']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display  = ['question', 'order', 'is_active']
    list_editable = ['order', 'is_active']


from .models import CoreValue, CEOMessage

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display  = ['title', 'icon', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(CEOMessage)
class CEOMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'is_active']