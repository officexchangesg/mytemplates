from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

# Create your models here.

class DJ_Howto(models.Model):
    howto = models.CharField(verbose_name='How To', max_length=100)
    # desc = models.TextField(verbose_name='Description', blank=True,null=True)
    description = HTMLField()
    tags = TaggableManager()

    class Meta:
        verbose_name = 'How To'
        verbose_name_plural = 'How-tos'

    def __str__(self):
        return self.howto


class DJ_Snippet(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    # desc = models.TextField(verbose_name='Description', blank=True,null=True)
    snippet = HTMLField()

    class Meta:
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'


class DJ_Concept(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    # desc = models.TextField(verbose_name='Description', blank=True,null=True)
    description = HTMLField(blank=True)
    is_Concept_Clear = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Concept'
        verbose_name_plural = 'Concepts'
