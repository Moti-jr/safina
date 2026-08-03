from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import DonationForm


class DonateView(FormView):
    template_name = 'donations/donate.html'
    form_class    = DonationForm
    success_url   = reverse_lazy('donations:donate')

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            'Thank you for your generosity! We will contact you shortly.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Please correct the errors below.'
        )
        return super().form_invalid(form)