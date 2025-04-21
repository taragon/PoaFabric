from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
# This is a view to redirect each individual to the rightful dashboard 
def login_redirect(request):
    if request.user.profile.role == 'recycler':
        return redirect('recycler_dashboard')
    else:
        return redirect('upcycler_dashboard')