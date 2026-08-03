from django.db import models
from django.utils.text import slugify


class NewsTag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title           = models.CharField(max_length=200)
    slug            = models.SlugField(unique=True, blank=True)
    summary         = models.CharField(max_length=300)
    body            = models.TextField()
    image           = models.ImageField(upload_to='news/')
    tags            = models.ManyToManyField(NewsTag, blank=True)
    is_featured     = models.BooleanField(default=False)
    is_published    = models.BooleanField(default=True)
    meta_description= models.CharField(max_length=300, blank=True)
    published_at    = models.DateField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title