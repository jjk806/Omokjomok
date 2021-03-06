from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from accounts.models import CustomUser
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
def tricksolving(request):
    pass

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

    if game.state.referee()[2] != 0: # 사람이 이겼을 경우
        if request.data['turn'] == '1':
            endmessage = 1
        else:
            endmessage = 2
        print(endmessage, '사람 승')
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

    legal, illegal, end = game.state.referee()
    
    if game.state.referee()[2] != 0: # AI가 이겼을 경우
        if request.data['turn'] == '1':
            endmessage = 2
        else:
            endmessage = 1
        print('AI 승')
        result = {'board': board, 'AIaction': AIaction, 'endmessage': endmessage, 'illegal': illegal}
        return Response(result)

    endmessage = -1
    for k in range(len(illegal)):
        x, y = illegal[k][0] // 15, illegal[k][0] % 15
        board[x][y] = 3

    result = {'board': board, 'AIaction': AIaction, 'endmessage': endmessage, 'illegal': illegal}

    return Response(result)

@api_view(['POST'])
def makeTrick(request):
    m_uid = request.data['pk']
    rows = TrickSolving(user=m_uid)
    rows.save()
    return Response()

@api_view(['POST'])
def Tricklist(request):
    user_id = request.data["pk"]
    tricks = get_object_or_404(TrickSolving, user=user_id)
    clear = [0]*15
    clear[0] = tricks.game1_1
    clear[1] = tricks.game1_2
    clear[2] = tricks.game1_3
    clear[3] = tricks.game1_4
    clear[4] = tricks.game1_5
    clear[5] = tricks.game2_1
    clear[6] = tricks.game2_2
    clear[7] = tricks.game2_3
    clear[8] = tricks.game2_4
    clear[9] = tricks.game2_5
    clear[10] = tricks.game3_1
    clear[11] = tricks.game3_2
    clear[12] = tricks.game3_3
    clear[13] = tricks.game3_4
    clear[14] = tricks.game3_5
    return Response(clear)



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
    pk = request.data["pk"]
    stage = request.data["stage"]
    trickSolve = get_object_or_404(TrickSolving, user=pk)
    user = get_object_or_404(CustomUser, id=pk)
    if stage == 11:
        trickSolve.game1_1 = 1
    elif stage == 12:
        trickSolve.game1_2 = 1
    elif stage == 13:
        trickSolve.game1_3 = 1
    elif stage == 14:
        trickSolve.game1_4 = 1
    elif stage == 15:
        trickSolve.game1_5 = 1
    elif stage == 21:
        trickSolve.game2_1 = 1
    elif stage == 22:
        trickSolve.game2_2 = 1
    elif stage == 23:
        trickSolve.game2_3 = 1
    elif stage == 24:
        trickSolve.game2_4 = 1
    elif stage == 25:
        trickSolve.game2_5 = 1
    elif stage == 31:
        trickSolve.game3_1 = 1
    elif stage == 32:
        trickSolve.game3_2 = 1
    elif stage == 33:
        trickSolve.game3_3 = 1
    elif stage == 34:
        trickSolve.game3_4 = 1
    elif stage == 35:
        trickSolve.game3_5 = 1
    trickSolve.save()
    score = trickSolve.game1_1 + trickSolve.game1_2 + trickSolve.game1_3 + trickSolve.game1_4 + trickSolve.game1_5
    score += trickSolve.game2_1 + trickSolve.game2_2 + trickSolve.game2_3 + trickSolve.game2_4 + trickSolve.game2_5
    score += trickSolve.game3_1 + trickSolve.game3_2 + trickSolve.game3_3 + trickSolve.game3_4 + trickSolve.game3_5
    user.score = score
    user.save()
    return Response()

@api_view(["Post"])
def ReadAllMyRecode(request):
    pk = request.data["pk"]
    recode = Recode.objects.filter(user=pk).order_by('-created_at')
    serializer = RecodeSerializer(recode, many=True)
    return Response(serializer.data)

@api_view(["Post"])
def ReadOneRecode(request):
    pk = request.data["pk"]
    recode = get_object_or_404(Recode, id=pk)
    serializer = RecodeSerializer(recode)
    return Response(serializer.data)

@api_view(["Post"])
def CreateRecode(request):
    user_id = request.data['pk']
    ai_level = request.data['level']
    turn = request.data['turn']
    recode = Recode(user=user_id, ailevel=ai_level, turn=turn)
    recode.save()
    return Response(recode.pk)

@api_view(["Post"])
def RecodeGameEdit(request):
    pk = request.data["pk"]
    game = request.data["game"]
    recode = get_object_or_404(Recode, id=pk)
    recode.game = recode.game + str(game) + " "
    recode.save()
    return Response()

@api_view(["Post"])
def RecodeWinEdit(request):
    pk = request.data["pk"]
    recode = get_object_or_404(Recode, id=pk)
    recode.win = 1
    recode.save()
    return Response()