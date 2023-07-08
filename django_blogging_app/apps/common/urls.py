from django.urls import path

from django_blogging_app.apps.common.views import index

urlpatterns = (
    path("", index, name="index"),
)
