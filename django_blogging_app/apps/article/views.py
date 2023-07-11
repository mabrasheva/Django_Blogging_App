from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

from django_blogging_app.apps.article.forms import ArticleCreateForm
from django_blogging_app.apps.article.models import Article


class DisabledFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'
            form.fields[field].widget.attrs['readonly'] = 'readonly'

        return form


# class ArticleForm(forms.ModelForm):
#     pass

# Forms:
# 1. Auto created based on `fields` (default)
# 2. `form_class` - return class
# 3. `get_form_class` - return class
# 4. `get_form` - return instance


class ArticleCreateView(LoginRequiredMixin, views.CreateView):
    model = Article
    template_name = "article/article_create.html"
    form_class = ArticleCreateForm
    success_url = reverse_lazy('index')


class ArticleListView(views.ListView):
    template_name = 'article/article_list.html'
    model = Article
    ordering = ['-created_on']
    paginate_by = 6


class ArticleDetailsView(views.DetailView):
    model = Article
    template_name = 'article/article_details.html'


class ArticleUpdateView(LoginRequiredMixin, DisabledFormFieldsMixin, views.UpdateView):
    model = Article
    template_name = "article/article_edit.html"
    fields = "__all__"

    # disabled_fields = ("author",)
    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.object.pk})


class ArticleDeleteView(LoginRequiredMixin, DisabledFormFieldsMixin, views.DeleteView):
    model = Article
    template_name = "article/article_delete.html"
    fields = "__all__"
    success_url = reverse_lazy('article_list')
