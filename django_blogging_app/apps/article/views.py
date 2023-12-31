from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from django_blogging_app.apps.article.forms import ArticleCreateForm, ArticleEditForm
from django_blogging_app.apps.article.models import Article
from django_blogging_app.apps.category.forms import CategoryFilterForm
from django_blogging_app.apps.category.models import Category
from django_blogging_app.apps.common.forms import CommentCreateForm, RatingForm
from django_blogging_app.apps.common.models import Comment, Rating

UserModel = get_user_model()


class ArticleActionsAuthorizedUserMixin(UserPassesTestMixin):
    model = Article
    success_url = reverse_lazy('article_list')

    def test_func(self):
        article = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return article.user == self.request.user or self.request.user.is_staff or self.request.user.is_superuser


class DisabledFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'
            form.fields[field].widget.attrs['readonly'] = 'readonly'

        return form


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

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q')
        if query:
            # If a search query is provided, filter articles by title, text, or author containing the query
            queryset = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(text__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()
        else:
            # If no search query is provided, show all articles
            queryset = self.model.objects.all()

        category_slug = self.request.GET.get('category')
        if category_slug:
            # If a category slug is provided, filter articles by the category
            queryset = queryset.filter(categories__slug=category_slug)

        form = CategoryFilterForm(self.request.GET)
        if form.is_valid() and form.cleaned_data['categories']:
            # If a category is selected in the filtering form, filter articles by the selected category
            category = form.cleaned_data['categories']
            queryset = queryset.filter(categories=category)

        user_id = self.request.GET.get('user')
        if user_id:
            # If a user ID is provided in the URL query parameters, filter articles by the user
            user = get_object_or_404(UserModel, pk=user_id)
            queryset = queryset.filter(user=user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_filter_form'] = CategoryFilterForm(self.request.GET)
        context['categories'] = Category.objects.all()  # Add all categories to the context
        return context


class ArticleDetailsView(views.DetailView):
    model = Article
    template_name = 'article/article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        context['comment_form'] = CommentCreateForm
        context['average_rating'] = article.average_rating
        context['rating_form'] = RatingForm()
        return context


class ArticleUpdateView(LoginRequiredMixin, DisabledFormFieldsMixin, ArticleActionsAuthorizedUserMixin,
                        views.UpdateView):
    model = Article
    template_name = "article/article_edit.html"
    form_class = ArticleEditForm

    # fields = ["title", "text", "categories"]

    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.object.pk})


class ArticleDeleteView(LoginRequiredMixin, DisabledFormFieldsMixin, ArticleActionsAuthorizedUserMixin,
                        views.DeleteView):
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


class ArticleRatingView(LoginRequiredMixin, views.CreateView):
    model = Rating
    template_name = 'article/article_rating.html'
    form_class = RatingForm

    def form_valid(self, form):
        user = self.request.user
        article = get_object_or_404(Article, pk=self.kwargs['pk'])

        # Check if the user has already rated the article
        try:
            rating = Rating.objects.get(article=article, user=user)
            rating.rating_value = form.cleaned_data['rating_value']  # Update the rating value
            rating.save()
        except Rating.DoesNotExist:
            # If the user has not rated the article before, create a new rating entry
            form.instance.user = user
            form.instance.article = article
            return super().form_valid(form)

        return HttpResponseRedirect(reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']}))

    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']})
