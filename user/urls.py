from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup')
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
    path('dashboard/', views.dashboard, name='dashboard')
    path('recycler/', views.recycler_dashboard, name='recycler_dashboard'),
    path( 'upcycler'/ views.upcycler_dashboard, name='upcycler_dashboard'),
]
