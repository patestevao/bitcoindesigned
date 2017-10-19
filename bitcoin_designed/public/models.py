from django.db import models
from django.utils import timezone


# Create your models here.
class Language(models.Model):

    name = models.CharField(
        "Language's name",
        max_length=70,
        blank=True,
        null=True,
    )

    code = models.CharField(
        "Language's code (5 characters max.)",
        max_length=5,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.code

    def __repr__(self):
        return "<Language: %s>" % self.code

    class Meta:
        ordering = ('code', 'name')


class Infographic(models.Model):

    pub_date = models.DateField(
        "Publication date",
        default=timezone.now,
    )
    last_update_date = models.DateField(
        "Last update date",
        default=timezone.now,
    )
    active = models.BooleanField(
        "Active",
        default=False,
    )
    title = models.CharField(
        "Title",
        max_length=140,
    )
    description = models.CharField(
        "Description",
        max_length=140,
    )
    sponsored = models.BooleanField(
        "Sponsored",
        default=False,
    )
    ad = models.BooleanField(
        "Ad",
        default=False,
    )
    slug = models.SlugField(
        "Slug",
    )
    medium_img = models.ImageField(
        "Medium image",
        max_length=500,
    )
    thumbnail_img = models.ImageField(
        "Thumbnail",
        max_length=500,
    )
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Infographic: %s>" % self.title

    def save(self, *args, **kwargs):
        self.last_update_date = timezone.now()
        super(Infographic, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-pub_date', 'title')


class InfographicURL(models.Model):

    url = models.URLField(
        "URL to high definition infographic",
        blank=True,
        null=True,
    )

    language = models.ForeignKey(
        Language, on_delete=models.CASCADE
    )

    infographic = models.ForeignKey(
        Infographic, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.url

    def __repr__(self):
        return "<InfographicURL: %s>" % self.url


class Tag(models.Model):

    tag = models.CharField(
        "Tag",
        max_length=20,
        blank=True,
        null=True,
    )
    description = models.CharField(
        "Description",
        max_length=150,
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        "Slug",
    )

    class Meta:
        ordering = ('tag',)

    def __repr__(self):
        return "<Tag: %s>" % self.tag

    def __str__(self):
        return self.tag
