import csv

from django.contrib import admin
from django.http import HttpResponse

from django_blogging_app.apps.article.models import Article


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="articles.csv"'
    writer = csv.writer(response)
    writer.writerow(['Title', 'User'])
    for article in queryset:
        writer.writerow([article.title, article.user])
    return response


export_to_csv.short_description = "Export selected articles to CSV"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "created_on")
    list_filter = ['categories', 'user']
    search_fields = ['title', 'text']
    actions = [export_to_csv]
    ordering = ['-created_on']
    sortable_by = ["id", "title", "user", "created_on"]
