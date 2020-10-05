from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import * 
from tensorflow.keras.models import load_model
from mcts import mcts_action
from game import Game

pb = load_model('./model/policy_black.h5', compile=False)
pw = load_model('./model/policy_white.h5', compile=False)
vb = load_model('./model/value_black_t.h5', compile=False)
vw = load_model('./model/value_white_t.h5', compile=False)


@api_view(['POST'])
def test(request):
    game = Game()
    board = request.data['board']
    black = [[0] * 15 for _ in range(15)]
    white = [[0] * 15 for _ in range(15)]
    for i in range(15):
        for j in range(15):
            if board[i][j] == 1:
                black[i][j] = 1
            elif board[i][j] == 2:
                white[i][j] = 1
    game.state.black = black
    game.state.white = white
    AIaction = mcts_action(pb, pw, vb, vw, game.state)
    c, r = AIaction//15, AIaction%15
    board[c][r] = 1 
    result = {'board': board, 'AIaction': AIaction}
    return Response(result)

@api_view(['GET'])
def Tricklist(request):
    tricks = TrickSolving.objects.filter(user=request.user)
    serializer = TrickSolvingSerializer(instance=tricks)
    return Response(serializer.data)
