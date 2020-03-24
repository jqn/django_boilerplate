from django.urls import path

from django.contrib.auth import views
from . import views as register_views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register_views.SignUpView.as_view(), name='register')
]
