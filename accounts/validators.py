from django.contrib.auth.validators import ASCIIUsernameValidator

class CustomUsernameValidator(ASCIIUsernameValidator):
    regex = r'^[\w.@+-]+$'
    message = 'Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.'

custom_username_validator = [CustomUsernameValidator()]