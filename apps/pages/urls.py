from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'pages'

urlpatterns = [
    path('',             views.HomeView.as_view(),       name='home'),
    path('about/',       views.AboutView.as_view(),      name='about'),
    path('mission/',     views.MissionView.as_view(),    name='mission'),
    path('vision/',      views.VisionView.as_view(),     name='vision'),
    path('history/',     views.HistoryView.as_view(),    name='history'),
    path('faq/',         views.FAQView.as_view(),        name='faq'),
    path('privacy/',     views.PrivacyView.as_view(),    name='privacy'),
    path('<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),

     # robots.txt
    path('robots.txt',
         TemplateView.as_view(
             template_name='robots.txt',
             content_type='text/plain'
         ),
         name='robots'),

    # Catch-all — must stay last
    path('<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
]
