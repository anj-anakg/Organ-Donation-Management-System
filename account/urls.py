from django.urls import path, re_path
from .views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    re_path(r'login/$', auth_views.LoginView.as_view(), name='login'),

]
