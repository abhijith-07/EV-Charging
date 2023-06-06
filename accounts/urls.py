from .views import *
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', home, name='home'),
    path('register/', CustomSignupView.as_view(), name='account_sign'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    
]
