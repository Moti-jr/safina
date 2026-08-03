from django.views.generic import ListView, DetailView
from .models import NewsArticle, NewsTag


class NewsListView(ListView):
    model               = NewsArticle
    template_name       = 'news/list.html'
    context_object_name = 'articles'
    paginate_by         = 9

    def get_queryset(self):
        queryset = NewsArticle.objects.filter(is_published=True)
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tags__slug=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags']        = NewsTag.objects.all()
        context['active_tag']  = self.request.GET.get('tag', '')
        return context


class NewsDetailView(DetailView):
    model               = NewsArticle
    template_name       = 'news/detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return NewsArticle.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = NewsArticle.objects.filter(
            is_published=True
        ).exclude(pk=self.object.pk)[:3]
        return context