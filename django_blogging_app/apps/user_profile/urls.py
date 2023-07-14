from django.urls import path

from django_blogging_app.apps.user_profile.views import RegisterUserView, LoginUserView, LogoutUserView, ListUsersView, \
    UserDetailsView, UserUpdateView, UserDeleteView

urlpatterns = (
    path("register/", RegisterUserView.as_view(), name="user_register"),
    path("login/", LoginUserView.as_view(), name="user_login"),
    path("logout/", LogoutUserView.as_view(), name="user_logout"),
    path("list/", ListUsersView.as_view(), name="users_list"),
    path("<int:pk>/", UserDetailsView.as_view(), name="user_details"),
    path("<int:pk>/edit/", UserUpdateView.as_view(), name="user_edit"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
)
