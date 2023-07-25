from django import forms

from django_blogging_app.apps.article.models import Article
from django_blogging_app.apps.category.models import Category


class ArticleBaseForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateForm(ArticleBaseForm):
    class Meta:
        model = Article
        exclude = ["user"]
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Title', },
            ),
            'text': forms.Textarea(
                attrs={'placeholder': 'Article content', }
            ),
            'categories': forms.CheckboxSelectMultiple()
        }


class ArticleEditForm(ArticleBaseForm):
    class Meta:
        model = Article
        exclude = ["user"]
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Title', },
            ),
            'text': forms.Textarea(
                attrs={'placeholder': 'Article content', }
            ),
            'categories': forms.CheckboxSelectMultiple()
        }
