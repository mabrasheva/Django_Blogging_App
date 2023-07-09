from django.urls import path

from django_blogging_app.apps.article.views import ArticleCreateView, ArticleListView, ArticleDetailsView

urlpatterns = (
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("list/", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailsView.as_view(), name="article_details"),
)
