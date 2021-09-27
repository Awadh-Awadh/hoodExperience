from django.urls import path
from django.contrib.auth import views
from .views import hero,home,register,profile, bist


urlpatterns = [
  path('',hero, name = 'hero'),
  path('register/',register,name = 'register'),
  path('login/',views.LoginView.as_view(template_name = 'hood/login.html'), name = 'login'),
  path('logout/', views.LogoutView.as_view(), name = 'logout'),
  path('home/',home, name ='home' ),
  path('profile/',profile, name = 'profile'),
  path('businesses/', bist, name= 'business' )

]