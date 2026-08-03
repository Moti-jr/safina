from django.views.generic import ListView, DetailView
from .models import Project, Category


class ProjectListView(ListView):
    model               = Project
    template_name       = 'projects/list.html'
    context_object_name = 'projects'
    paginate_by         = 9

    def get_queryset(self):
        return Project.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProjectDetailView(DetailView):
    model               = Project
    template_name       = 'projects/detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Project.objects.filter(
            category=self.object.category,
            is_published=True
        ).exclude(pk=self.object.pk)[:3]
        return context


class ProjectByCategoryView(ListView):
    model               = Project
    template_name       = 'projects/list.html'
    context_object_name = 'projects'
    paginate_by         = 9

    def get_queryset(self):
        return Project.objects.filter(
            category__slug=self.kwargs['slug'],
            is_published=True
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']        = Category.objects.all()
        context['active_category']   = self.kwargs['slug']
        return context