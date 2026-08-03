from django.db import models
from django.utils.text import slugify


class Page(models.Model):
    """Generic flat page — About, Mission, Vision, History etc."""
    title           = models.CharField(max_length=200)
    slug            = models.SlugField(unique=True, blank=True)
    body            = models.TextField()
    meta_title      = models.CharField(max_length=200, blank=True)
    meta_description= models.CharField(max_length=300, blank=True)
    banner_image    = models.ImageField(upload_to='pages/', blank=True)
    is_published    = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class MilestoneEvent(models.Model):
    """Timeline entries on the History page."""
    year        = models.PositiveIntegerField()
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to='history/', blank=True)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['year', 'order']

    def __str__(self):
        return f'{self.year} — {self.title}'