from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['POST'])
def test(request):
    # print("도착했어요")
    # print(request.data)

    # print("asd")
    # return Response("asd")
    # //////////////////////////
    board = request.data['board']
    print(board)
    ch = 0
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                ch = 1
                board[i][j] = 2
                break
        if ch == 1:
            break
    print(board)
    return Response(board)
   # //////////////////////////
