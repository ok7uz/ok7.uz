from django.db import models
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True)

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    tags = models.ManyToManyField(Tag, related_name='projects')
    started_date = models.DateField()
    finished_date = models.DateField(null=True)

    class Meta:
        db_table = 'project'
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ('-finished_date',)

    def __str__(self):
        return self.name
