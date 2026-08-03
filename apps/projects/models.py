from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Project categories — Education, Healthcare, etc."""
    name    = models.CharField(max_length=100)
    slug    = models.SlugField(unique=True, blank=True)
    icon    = models.CharField(max_length=50, blank=True,
                               help_text='Font Awesome class e.g. fa-graduation-cap')
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    """Individual projects managed by Safina Initiative."""

    STATUS_CHOICES = [
        ('ongoing',   'Ongoing'),
        ('completed', 'Completed'),
        ('upcoming',  'Upcoming'),
    ]

    title           = models.CharField(max_length=200)
    slug            = models.SlugField(unique=True, blank=True)
    category        = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                        null=True, related_name='projects')
    summary         = models.CharField(max_length=300)
    description     = models.TextField()
    image           = models.ImageField(upload_to='projects/')
    status          = models.CharField(max_length=20,
                                       choices=STATUS_CHOICES, default='ongoing')
    beneficiaries   = models.PositiveIntegerField(default=0)
    location        = models.CharField(max_length=200, blank=True)
    start_date      = models.DateField(null=True, blank=True)
    end_date        = models.DateField(null=True, blank=True)
    is_featured     = models.BooleanField(default=False)
    is_published    = models.BooleanField(default=True)
    meta_description= models.CharField(max_length=300, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title