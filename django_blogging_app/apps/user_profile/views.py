from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from django_blogging_app.apps.user_profile.forms import RegisterUserForm

UserModel = get_user_model()


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


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = "user_profile/user_details.html"
    model = UserModel

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["articles_count"] = self.request.user.article_set.all()
    #     return context


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = "user_profile/user_delete.html"
