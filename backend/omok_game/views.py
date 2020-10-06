from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import * 
from tensorflow.keras.models import load_model
from mcts import mcts_action as mcts_high
from mcts_middle import mcts_action as mcts_middle
from mcts_low import mcts_action as mcts_low
from game import Game

pb = load_model('./model/policy_black.h5', compile=False)
pw = load_model('./model/policy_black.h5', compile=False)
vb = load_model('./model/value_black_t.h5', compile=False)
vw = load_model('./model/value_black_t.h5', compile=False)


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

    if game.state.referee()[2] != 0:
        endmessage = 1
        result = {'board': board, 'AIaction': -1, 'endmessage': endmessage}
        return Response(result)

    if request.data['turn'] == '1':
        game.state.turn = [[1]]
    else:
        game.state.turn = [[0]]

    if request.data['level'] == '0':
        AIaction = mcts_low(pb, pw, vb, vw, game.state)
    elif request.data['level'] == '1':
        AIaction = mcts_middle(pb, pw, vb, vw, game.state)
    elif request.data['level'] == '2':
        AIaction = mcts_high(pb, pw, vb, vw, game.state)

    c, r = AIaction//15, AIaction%15
    if request.data['turn'] == '1':
        board[c][r] = 2
    else:
        board[c][r] = 1

    for i in range(15):
        for j in range(15):
            if board[i][j] == 1:
                black[i][j] = 1
            elif board[i][j] == 2:
                white[i][j] = 1
    game.state.black = black
    game.state.white = white

    if game.state.referee()[2] != 0:
        endmessage = 2
        result = {'board': board, 'AIaction': AIaction, 'endmessage': endmessage}
        return Response(result)

    endmessage = -1
    result = {'board': board, 'AIaction': AIaction, 'endmessage': endmessage}
    return Response(result)

@api_view(['GET'])
def Tricklist(request):
    pk = request.data["pk"]
    tricks = TrickSolving.objects.filter(user=pk)
    serializer = TrickSolvingSerializer(instance=tricks)
    return Response(serializer.data)



@api_view(['POST'])
def gamestart(request):
    rsgame = omokgame.objects.all()
    g_data = request.data['data']
    g_auid = request.data['auid']
    g_turn = request.data['turn']
    g_date = request.data['date']

    rows = omokgame.object.create(data = g_data, auid = g_auid, turn = g_turn, date = g_date)


@api_view(['POST'])
def showgame(request):
    round = request.data['round']
    rsgame = myosu.objects.get(round = round)
    arr = list(rsgame.data.split())
    for i in range(len(arr)):
        arr[i] = arr[i][0] + chr(int(arr[i][1:]) + 96)

    return Response(arr)


@api_view(['POST'])
def makeroom(request):
    rsgame = room.objects.all()
    r_uid = request.data['uid']
    r_att_turn = request.data['att_turn']
    r_level = request.data['level']

    rows = room.object.create(uid = r_uid, att_turn = r_att_turn, level = r_level)

@api_view(['POST'])
def myosuWin(request):
    # pk = request.data["pk"]
    # stage = request.data["stage"]
    # trickSolve = TrickSolving.get_object_or_404(TrickSolving, user=pk)
    # if stage == game1:
    # trickSolve."game1"
    return Response()
