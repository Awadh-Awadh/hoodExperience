from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser,Profile


class CustormUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = ('first_name','last_name','username','email')

class EditProfile(forms.ModelForm):
        class Meta:
            model = Profile
            exclude = ('user',)