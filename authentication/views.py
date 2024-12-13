from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

# Sign-up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Specify the backend explicitly
            backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user, backend=backend)
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')  # Redirect to login page after successful signup
        else:
            messages.error(request, "Error creating account. Please check the form.")
    else:
        form = UserCreationForm()

    return render(request, 'portal/register.html', {'form': form})





# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to the homepage
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')
