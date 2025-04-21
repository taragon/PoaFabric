from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required 

# Create your views here.
# This is a view to redirect each individual to the rightful dashboard 
def login_redirect(request):
    if request.user.profile.role == 'recycler':
        return redirect('recycler_dashboard')
    else:
        return redirect('upcycler_dashboard')
    

@login_required
def recycler_dashboard(request):
    # show recyclable items that is in recyclable.html
    return render(request, 'user/recycler.html')

@login_required
def upcycler_dashboard(request):
    #Show upcycaled items that is in upcycler.html
    return render(request, 'user/upcycler.html')

# creating homepage function
def home(request):
    return render(request, 'user/home.html')


    


