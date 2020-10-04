from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('emailAuth/', views.emailAuth),
    path('login/kakao/', views.kakao_login, name='kakao_login'),
    path('login/kakao/callback/', views.kakao_callback, name='kakao_callback'),
]