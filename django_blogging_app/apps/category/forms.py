from django import forms
from django_blogging_app.apps.category.models import Category


class CategoryFilterForm(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='All',
        required=False,
        # widget=forms.Select(attrs={'id': 'category'}),
    )
