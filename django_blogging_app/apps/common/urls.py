from django.urls import path

from django_blogging_app.apps.common.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
)
