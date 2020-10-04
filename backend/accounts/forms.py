from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import get_user_model
 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
