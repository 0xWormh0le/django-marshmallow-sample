from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    regions = models.ManyToManyField(
        'regions.Region', related_name='articles', blank=True
    )
    author = models.ForeignKey(
        'authors.Author', on_delete=models.CASCADE, blank=True, null=True
    )
