from django.urls import path

from django_blogging_app.apps.article.views import ArticleCreateView, ArticleListView, ArticleDetailsView, \
    ArticleUpdateView, ArticleDeleteView

urlpatterns = (
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("list/", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailsView.as_view(), name="article_details"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
)
