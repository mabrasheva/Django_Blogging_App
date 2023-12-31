from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "password1", "password2", "email",)
        consent = forms.BooleanField(
            label="I accept the Terms and Conditions "
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = ""
