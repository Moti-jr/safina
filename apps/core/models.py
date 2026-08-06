from django.db import models

class SiteSettings(models.Model):
    """Global site settings — only one row should exist."""
    site_name        = models.CharField(max_length=100, default='Safina Initiative')
    tagline          = models.CharField(max_length=200, blank=True)
    email            = models.EmailField(blank=True)
    phone            = models.CharField(max_length=20, blank=True)
    address          = models.TextField(blank=True)
    facebook         = models.URLField(blank=True)
    twitter          = models.URLField(blank=True)
    instagram        = models.URLField(blank=True)
    youtube          = models.URLField(blank=True)
    logo             = models.ImageField(upload_to='core/', blank=True)
    favicon          = models.ImageField(upload_to='core/', blank=True)
    footer_text      = models.TextField(blank=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name


class HeroSlide(models.Model):
    """Homepage hero carousel slides."""
    title       = models.CharField(max_length=200)
    subtitle    = models.TextField(blank=True)
    image       = models.ImageField(upload_to='hero/')
    btn_label   = models.CharField(max_length=50, blank=True)
    btn_url     = models.CharField(max_length=200, blank=True)
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Statistic(models.Model):
    """Animated numbers on homepage — e.g. 500 Beneficiaries."""
    label       = models.CharField(max_length=100)
    value       = models.PositiveIntegerField()
    icon        = models.CharField(max_length=50, blank=True,
                                   help_text='Font Awesome class e.g. fa-users')
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.value} {self.label}'


class Testimonial(models.Model):
    """Quotes from beneficiaries or partners."""
    name        = models.CharField(max_length=100)
    role        = models.CharField(max_length=100, blank=True)
    quote       = models.TextField()
    photo       = models.ImageField(upload_to='testimonials/', blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} — {self.role}'


class TeamMember(models.Model):
    """Staff and board members."""
    name        = models.CharField(max_length=100)
    role        = models.CharField(max_length=100)
    bio         = models.TextField(blank=True)
    photo       = models.ImageField(upload_to='team/', blank=True)
    email       = models.EmailField(blank=True)
    linkedin    = models.URLField(blank=True)
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name} — {self.role}'


class FAQ(models.Model):
    """Frequently asked questions."""
    question    = models.CharField(max_length=300)
    answer      = models.TextField()
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'

    def __str__(self):
        return self.question



class CoreValue(models.Model):
    """What Drives Us section — core values of the organisation."""
    title       = models.CharField(max_length=100)
    description = models.TextField()
    icon        = models.CharField(max_length=50, blank=True,
                                   help_text='Font Awesome class e.g. fa-heart')
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class CEOMessage(models.Model):
    """CEO / Executive Director remarks shown on homepage."""
    name        = models.CharField(max_length=100)
    title       = models.CharField(max_length=100,
                                   default='Executive Director')
    message     = models.TextField()
    photo       = models.ImageField(upload_to='team/', blank=True)
    signature   = models.ImageField(upload_to='team/', blank=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'CEO Message'

    def __str__(self):
        return f'{self.name} — {self.title}'