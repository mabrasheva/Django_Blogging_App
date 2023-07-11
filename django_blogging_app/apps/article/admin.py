from django.contrib import admin

from django_blogging_app.apps.article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
