from django.db import models


class DonationInquiry(models.Model):

    TYPE_CHOICES = [
        ('one_time',   'One-time Donation'),
        ('monthly',    'Monthly Donation'),
        ('in_kind',    'In-kind Donation'),
        ('partner',    'Partnership'),
    ]

    STATUS_CHOICES = [
        ('pending',    'Pending'),
        ('contacted',  'Contacted'),
        ('completed',  'Completed'),
    ]

    name            = models.CharField(max_length=100)
    email           = models.EmailField()
    phone           = models.CharField(max_length=20, blank=True)
    donation_type   = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount          = models.DecimalField(max_digits=10, decimal_places=2,
                                          null=True, blank=True)
    message         = models.TextField(blank=True)
    status          = models.CharField(max_length=20,
                                       choices=STATUS_CHOICES, default='pending')
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering    = ['-created_at']
        verbose_name = 'Donation Inquiry'
        verbose_name_plural = 'Donation Inquiries'

    def __str__(self):
        return f'{self.name} — {self.donation_type}'