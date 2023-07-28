from django import forms

from django_blogging_app.apps.article.models import Article


class ArticleBaseForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["user"]
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Title',
                       "class": "form-control",
                       },
            ),
            'text': forms.Textarea(
                attrs={'placeholder': 'Article content',
                       "class": "form-control",
                       }
            ),
            'categories': forms.CheckboxSelectMultiple()
        }


class ArticleCreateForm(ArticleBaseForm):
    pass


class ArticleEditForm(ArticleBaseForm):
    pass
