from django import forms

from django_blogging_app.apps.article.models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Title', },
            ),
            'text': forms.Textarea(
                attrs={'placeholder': 'Article content', }
            ),
        }