from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def test(request):
    board = request.data
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