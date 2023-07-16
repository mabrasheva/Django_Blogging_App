from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

from django_blogging_app.apps.article.forms import ArticleCreateForm
from django_blogging_app.apps.article.models import Article
from django_blogging_app.apps.common.forms import CommentCreateForm
from django_blogging_app.apps.common.models import Comment


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

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class ArticleListView(views.ListView):
    template_name = 'article/article_list.html'
    model = Article
    ordering = ['-created_on']
    paginate_by = 6


class ArticleDetailsView(views.DetailView):
    model = Article
    template_name = 'article/article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentCreateForm
        return context


class ArticleUpdateView(LoginRequiredMixin, DisabledFormFieldsMixin, views.UpdateView):
    model = Article
    template_name = "article/article_edit.html"
    fields = ["title", "text"]

    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.object.pk})


class ArticleDeleteView(LoginRequiredMixin, DisabledFormFieldsMixin, views.DeleteView):
    model = Article
    template_name = "article/article_delete.html"
    fields = "__all__"
    success_url = reverse_lazy('article_list')


class ArticleCommentView(LoginRequiredMixin, views.CreateView):
    model = Comment
    template_name = "common/comment_create.html"
    form_class = CommentCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']})
