from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import SigUpForm


def register(request):
    if request.method == "POST":
        form = SigUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    form = SigUpForm()
    return render(request, "register.html", {"form": form})

@login_required()
def profile(request):
    return render(request, "profile.html")

