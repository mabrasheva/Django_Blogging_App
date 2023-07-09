from django.urls import reverse_lazy
from django.views import generic as views

from django_blogging_app.apps.article.models import Article


class ArticleCreateView(views.CreateView):
    model = Article
    template_name = "article/article_create.html"
    fields = "__all__"
    success_url = reverse_lazy('index')


class ArticleListView(views.ListView):
    template_name = 'article/article_list.html'
    model = Article
    ordering = ['-created_on']
    paginate_by = 6


class ArticleDetailsView(views.DetailView):
    model = Article
    template_name = 'article/article_details.html'
