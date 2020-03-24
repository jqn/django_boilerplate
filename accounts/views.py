from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SignUpForm

# Create your views here.


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = SignUpForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return redirect('/accounts/login/')
