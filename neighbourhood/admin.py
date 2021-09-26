from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustormUserCreationForm
from .models import CustomUser, Neighbourhood, Business,Profile, Posts

# Register your models here.
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustormUserCreationForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'username']
models = [ Neighbourhood, Business,Profile, Posts]
admin.site.register(CustomUser,CustomUserAdmin)
for model in models:
    admin.site.register(model)