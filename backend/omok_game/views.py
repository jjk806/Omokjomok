from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mcts import mcts_action
from game import Game

# pb = load_model('./model/policy_black.h5', compile=False)
# pw = load_model('./model/policy_white.h5', compile=False)
# vb = load_model('./model/value_black_t.h5', compile=False)
# vw = load_model('./model/value_white_t.h5', compile=False)

# Create your views here.
@api_view(['POST'])
def test(request):
    print('clear', request.data['board'])
    board = request.data['board']
    # AIaction = mcts_action(pb, pw, vb, vw, game.state)
    # c, r = AIaction//15, AIaction%15
    # board[c][r] = 1 
    return Response(board)