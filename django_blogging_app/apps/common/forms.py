from django import forms

from django_blogging_app.apps.common.models import Comment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]
