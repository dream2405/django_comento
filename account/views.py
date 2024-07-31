from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignupForm


def my_page(request):
    return render(request, 'mypage.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
