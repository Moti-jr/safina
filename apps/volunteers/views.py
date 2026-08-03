from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import VolunteerForm


class VolunteerView(FormView):
    template_name = 'volunteers/volunteer.html'
    form_class    = VolunteerForm
    success_url   = reverse_lazy('volunteers:volunteer')

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            'Thank you for applying! We will be in touch soon.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Please correct the errors below.'
        )
        return super().form_invalid(form)