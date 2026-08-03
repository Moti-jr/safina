from django.views.generic import TemplateView, DetailView
from apps.core.models import (
    HeroSlide, Statistic, Testimonial, TeamMember, FAQ
)
from apps.projects.models import Project
from apps.news.models import NewsArticle
from apps.pages.models import Page, MilestoneEvent


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Database content
        context['slides']       = HeroSlide.objects.filter(is_active=True)
        context['stats']        = Statistic.objects.filter(is_active=True)
        context['testimonials'] = Testimonial.objects.filter(is_active=True)
        context['projects']     = Project.objects.filter(
                                    is_featured=True, is_published=True)[:3]
        context['news']         = NewsArticle.objects.filter(
                                    is_published=True)[:3]

        # Fallback defaults shown before admin adds real content
        context['default_stats'] = [
            {'icon': 'fa-users',         'value': 500,  'label': 'Beneficiaries'},
            {'icon': 'fa-graduation-cap','value': 120,  'label': 'Students Supported'},
            {'icon': 'fa-heart-pulse',   'value': 80,   'label': 'Health Outreaches'},
            {'icon': 'fa-handshake',     'value': 15,   'label': 'Partner Organisations'},
        ]
        context['default_projects'] = [
            {'icon': 'fa-graduation-cap', 'category': 'Education',
             'title': 'School Bursary Program',
             'desc': 'Supporting bright students from low-income families with full bursaries.'},
            {'icon': 'fa-heart-pulse',    'category': 'Healthcare',
             'title': 'Mobile Health Clinics',
             'desc': 'Bringing essential healthcare services directly to remote communities.'},
            {'icon': 'fa-venus',          'category': 'Women & Girls',
             'title': 'Girls Empowerment',
             'desc': 'Mentorship, skills training, and support for young women to thrive.'},
        ]
        context['focus_areas'] = [
            {'icon': 'fa-graduation-cap', 'title': 'Education',
     'color': '#4ade80',
     'desc': 'Quality learning for every child, from early years through secondary school.'},
            {'icon': 'fa-heart-pulse', 'title': 'Healthcare',
     'color': '#F4B400',
     'desc': 'Accessible health services and preventative care for entire families.'},
            {'icon': 'fa-venus', 'title': 'Women & Girls',
     'color': '#a78bfa',
     'desc': 'Empowering women and girls to lead, earn, and shape their communities.'},
            {'icon': 'fa-seedling', 'title': 'Community',
     'color': '#34d399',
     'desc': 'Sustainable livelihoods and infrastructure built from within.'},
        ]
        context['default_testimonials'] = [
            {
        'name': 'Amina Wanjiru',
        'role': 'Scholarship Beneficiary, Nairobi',
        'quote': 'Safina Initiative gave me the chance to finish school when my family could not afford the fees. Today I am in university studying nursing.',
            },
            {
        'name': 'James Otieno',
        'role': 'Community Leader, Kisumu',
        'quote': 'The mobile health clinic came to our village for the first time last year. Over 200 families received care they had never had access to before.',
            },
            {
        'name': 'Grace Muthoni',
        'role': 'Women\'s Group Member, Nakuru',
        'quote': 'Through the women\'s empowerment program I started my own business. I now employ three other women from my community.',
            },
        ]
        return context
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides']       = HeroSlide.objects.filter(is_active=True)
        context['stats']        = Statistic.objects.filter(is_active=True)
        context['testimonials'] = Testimonial.objects.filter(is_active=True)
        context['team']         = TeamMember.objects.filter(is_active=True)[:4]
        context['projects']     = Project.objects.filter(
                                    is_featured=True,
                                    is_published=True)[:3]
        context['news']         = NewsArticle.objects.filter(
                                    is_published=True)[:3]
        return context


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = TeamMember.objects.filter(is_active=True)
        return context


class MissionView(TemplateView):
    template_name = 'pages/mission.html'


class VisionView(TemplateView):
    template_name = 'pages/vision.html'


class HistoryView(TemplateView):
    template_name = 'pages/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['milestones'] = MilestoneEvent.objects.all()
        return context


class FAQView(TemplateView):
    template_name = 'pages/faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = FAQ.objects.filter(is_active=True)
        return context


class PrivacyView(TemplateView):
    template_name = 'pages/privacy.html'


class PageDetailView(DetailView):
    model               = Page
    template_name       = 'pages/page_detail.html'
    context_object_name = 'page'
    slug_field          = 'slug'

    def get_queryset(self):
        return Page.objects.filter(is_published=True)