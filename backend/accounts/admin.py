from django.contrib import admin
from .models import CustomUser
# from .forms import CustomUserCreationForm, CustomUserChangeForm
  
admin.site.register(CustomUser)