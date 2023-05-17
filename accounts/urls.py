from .views import home, CustomSignupView
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', home, name='home'),
    path('register/', CustomSignupView.as_view(), name='account_sign'),
]
