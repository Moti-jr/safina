from django.db import models


class ContactMessage(models.Model):

    STATUS_CHOICES = [
        ('unread',   'Unread'),
        ('read',     'Read'),
        ('replied',  'Replied'),
    ]

    name        = models.CharField(max_length=100)
    email       = models.EmailField()
    subject     = models.CharField(max_length=200)
    message     = models.TextField()
    status      = models.CharField(max_length=20,
                                   choices=STATUS_CHOICES, default='unread')
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject}'