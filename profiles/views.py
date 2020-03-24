from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, UpdateView
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


class ProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile.html'
    success_url = "/"
