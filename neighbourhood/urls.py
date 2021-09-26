from django.urls import path
from django.contrib.auth import views
from .views import hero


urlpatterns = [
  path('',hero, name = 'hero'),
  path('login/',views.LoginView.as_view(template_name = 'hood/login.html'), name = 'login'),
  path('logout/', views.LogoutView.as_view(), name = 'logout')


]