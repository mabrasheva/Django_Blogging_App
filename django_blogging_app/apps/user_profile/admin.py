from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_filter = ['is_superuser', 'is_staff', 'groups']
    ordering = ['username']
    search_fields = ['username']

    # Customizing the save_model method to handle password hashing
    def save_model(self, request, obj, form, change):
        # If a password is provided, set it using set_password
        if 'password' in form.data and form.data['password']:
            obj.set_password(form.data['password'])
        obj.save()
