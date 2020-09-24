from django.urls import path
from . import views

app_name = 'omok_game'

urlpatterns = [
    path('testgame/', views.test),  # 시험용
]
