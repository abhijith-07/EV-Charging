from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import CreateUserForm, CustomSignupForm
from allauth.account.views import SignupView

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        context = {'username': username}
        return render(request, 'accounts/index.html', context)
    else:
        return render(request, 'accounts/index.html')
        

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("Valid Form Got")
            form.save()
            return redirect('home')
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

class CustomSignupView(SignupView):
    def __init__(self):
        form = CustomSignupForm()
        if form.is_valid():
                print("Valid Form Got")
                form.save()
                return redirect('home')
        else:
            form = CustomSignupForm()