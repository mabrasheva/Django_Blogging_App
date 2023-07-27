from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from django_blogging_app.apps.user_profile.forms import RegisterUserForm

UserModel = get_user_model()


class UserDeleteMixin(UserPassesTestMixin):
    model = UserModel
    success_url = reverse_lazy('user_list')

    def test_func(self):
        user = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return user == self.request.user or self.request.user.is_superuser


class UserChangePasswordMixin(UserPassesTestMixin):
    model = UserModel
    success_url = reverse_lazy('user_list')

    def test_func(self):
        user = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return user == self.request.user


class RegisterUserView(views.CreateView):
    template_name = "user_profile/user_register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'user_profile/user_login.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class ListUsersView(LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'user_profile/users_list.html'
    paginate_by = 20


class UserUpdateView(LoginRequiredMixin, views.UpdateView):
    template_name = "user_profile/user_edit.html"
    model = UserModel
    fields = ["first_name", "last_name", "email", "profile_image"]

    def get_success_url(self):
        return reverse_lazy('user_details', kwargs={'pk': self.object.pk})


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = "user_profile/user_details.html"
    model = UserModel


class UserDeleteView(LoginRequiredMixin, UserDeleteMixin, views.DeleteView):
    template_name = "user_profile/user_delete.html"
    model = UserModel
    success_url = reverse_lazy('index')


class UserChangePasswordView(LoginRequiredMixin, UserChangePasswordMixin, auth_views.PasswordChangeView):
    template_name = 'user_profile/user_change_password.html'
    success_url = reverse_lazy('user_change_password_done')

# ToDo user change profile image from url to upload file
# ToDo signal for sending mail when a user is registered
