from django.views.generic import TemplateView
from .models import GalleryImage, GalleryCategory, Video


class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GalleryCategory.objects.all()
        context['images']     = GalleryImage.objects.filter(is_active=True)
        return context


class VideoView(TemplateView):
    template_name = 'gallery/videos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(is_active=True)
        return context