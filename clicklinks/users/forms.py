from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = AbstractUser
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Используется встроенная модель User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
