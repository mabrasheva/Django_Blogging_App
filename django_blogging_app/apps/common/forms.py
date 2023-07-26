from django import forms

from django_blogging_app.apps.common.models import Comment, Rating


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating_value"]

    rating_value = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect(),
    )
