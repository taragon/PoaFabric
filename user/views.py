from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .forms import SignupForm
from .models import Profile, Item
from django.views.decorators.csrf import csrf_exempt



# creating homepage function
def home(request):
    return render(request, 'user/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user, role=role)
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'user/signup.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'user/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid credentials'})

    return render(request, 'user/login.html')



# function for loging out
def logout_view( request):
    logout(request)
    return redirect('home')

#return user Login
@login_required
def dashboard(request):
    role = request.user.profile.role
    if role == 'recycler':
        return redirect('recycler_dashboard')
    elif role == 'upcycler':
        return redirect('upcycler_dashboard')
    
#Function to redirect user to recycler dashboard
@login_required
def recycler_dashboard(request):
    items = Item.objects.filter(posted_by=request.user)
    return render(request, 'user/recycler.html', {'items': items})

#function to redirect user to upcycler dashboard
@login_required
def upcycler_dashboard(request):
    items = Item.objects.all()
    return render(request, 'user/upcycler.html', {'items': items})

