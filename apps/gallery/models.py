from django.db import models


class GalleryCategory(models.Model):
    name    = models.CharField(max_length=100)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Gallery Categories'

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title       = models.CharField(max_length=200, blank=True)
    image       = models.ImageField(upload_to='gallery/')
    category    = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name='images')
    caption     = models.CharField(max_length=300, blank=True)
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title or f'Image {self.pk}'


class Video(models.Model):
    title       = models.CharField(max_length=200)
    youtube_url = models.URLField(help_text='Full YouTube URL')
    thumbnail   = models.ImageField(upload_to='videos/', blank=True)
    description = models.TextField(blank=True)
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def embed_url(self):
        """Convert YouTube watch URL to embed URL automatically."""
        if 'watch?v=' in self.youtube_url:
            video_id = self.youtube_url.split('watch?v=')[-1].split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        return self.youtube_url