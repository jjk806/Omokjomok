from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def test(request):
    print('clear', reques.data['board'])
    board = request.data['board']
    ch = 0
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                ch = 1
                board[i][j] = 1
                break
        if ch == 1:
            break
    return Response(board)