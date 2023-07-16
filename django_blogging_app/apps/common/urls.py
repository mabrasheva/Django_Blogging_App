from django.urls import path
from django.views.generic import RedirectView

from django_blogging_app.apps.common.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
    path("admin/", RedirectView.as_view(), name="admin_panel"),
)
