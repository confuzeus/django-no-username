from django.contrib.auth.forms import (
    UserChangeForm as DefaultUserChangeForm,
    UserCreationForm as DefaultUserCreationForm,
)

from accounts.models import User


class UserChangeForm(DefaultUserChangeForm):

    class Meta:
        model = User
        fields = "__all__"


class UserCreationForm(DefaultUserCreationForm):

    class Meta:
        model = User
        fields = ["email"]
