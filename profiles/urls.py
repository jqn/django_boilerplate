from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('<int:pk>/', login_required(views.ProfileView.as_view()), name='profiles'),

]
