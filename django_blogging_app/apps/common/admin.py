from django.contrib import admin

from django_blogging_app.apps.common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "comment_text", "user")
