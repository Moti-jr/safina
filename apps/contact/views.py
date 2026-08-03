from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class    = ContactForm
    success_url   = reverse_lazy('contact:contact')

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            'Thank you for reaching out! We will get back to you soon.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Please correct the errors below.'
        )
        return super().form_invalid(form)