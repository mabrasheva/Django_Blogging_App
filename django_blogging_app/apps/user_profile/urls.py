from django.urls import path

from django_blogging_app.apps.user_profile.views import user_register, user_login, user_logout

urlpatterns = (
    path("register/", user_register, name="user_register"),
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
)
