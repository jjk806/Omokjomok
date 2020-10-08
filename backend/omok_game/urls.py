from django.urls import path
from . import views

app_name = 'omok_game'

urlpatterns = [
    path('testgame/', views.test), # 시험용
    path('tricklist/', views.Tricklist),
    path('gamestart/', views.gamestart),
    path('myosu/', views.showgame),
    path('room/', views.makeroom),
    path('myosuwin/', views.myosuWin),
    path('maketrick/', views.makeTrick),
    path('tricksolving/', views.tricksolving),
    path('readallmyrecode/', views.ReadAllMyRecode)
]