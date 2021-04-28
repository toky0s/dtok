from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from . import views


app_name='home'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('register/', views.register, name='register'),
    path('register_success/',views.register_success, name='register_success')
]