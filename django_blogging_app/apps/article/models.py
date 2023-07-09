from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(
        blank=False,
        null=False,
    )
    text = models.TextField(
        blank=False,
        null=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    # ToDo
    # author = models.OneToOneField()
    # category
    # tags

    class Meta:
        ordering = ['created_on']

    def get_absolute_url(self):
        return reverse('article_details', args=[str(self.pk)])
