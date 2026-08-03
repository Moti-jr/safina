from django.db import models


class VolunteerApplication(models.Model):

    SKILL_CHOICES = [
        ('teaching',    'Teaching & Training'),
        ('healthcare',  'Healthcare'),
        ('tech',        'Technology'),
        ('admin',       'Administration'),
        ('comms',       'Communications'),
        ('other',       'Other'),
    ]

    STATUS_CHOICES = [
        ('pending',  'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]

    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.EmailField()
    phone           = models.CharField(max_length=20, blank=True)
    skills          = models.CharField(max_length=50, choices=SKILL_CHOICES)
    availability    = models.CharField(max_length=200)
    motivation      = models.TextField()
    status          = models.CharField(max_length=20,
                                       choices=STATUS_CHOICES, default='pending')
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name} — {self.status}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'