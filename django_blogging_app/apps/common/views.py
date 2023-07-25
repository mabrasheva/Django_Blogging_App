from django.views import generic as views

from django_blogging_app.apps.article.models import Article
from django_blogging_app.apps.category.models import Category


class IndexView(views.TemplateView):
    template_name = "common/index.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()
        categories = Category.objects.all()

        if articles:
            context['featured_article'] = Article.objects.order_by('-created_on')[0]
            articles_count = articles.count()
            if 0 < articles_count < 3:
                context['articles'] = Article.objects.order_by('-created_on')[1:articles_count]
            else:
                context['articles'] = Article.objects.order_by('-created_on')[1:3]

        if categories:
            context['categories'] = Category.objects.order_by('name')

        return context
