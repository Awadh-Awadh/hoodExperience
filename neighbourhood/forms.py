from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustormUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = ('first_name','last_name','username','email')