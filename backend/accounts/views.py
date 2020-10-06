from django.shortcuts import render, redirect, get_object_or_404 
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMessage
# from rest_framework_jwt.utils import jwt_decode_handler
from .models import *
from .serializers import *

import random
import urllib 

# Create your views here.
@api_view(['POST'])
def emailAuth(request):
    number = random.randrange(100000, 1000000)
    email = request.data['email'] # 받는 사람 이메일
    exists_email = CustomUser.objects.filter(email=email)
    print(exists_email)
    if exists_email:
        number = 0
    else:
        subject = '오목조목 회원 인증 메일' # 제목
        message = '인증하실 번호는' + str(number) + '입니다.' # 내용
        sendmail = EmailMessage(subject, message, to=[email])
        # EmailMessage(제목, 내용, 보내는 사람(settings 설정으로 안 적어도 됨), 받는 사람 목록)
        sendmail.send()
    return Response(number)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userPlay(request):
    user_id = request.data['pk']
    user = get_object_or_404(CustomUser, id=user_id)
    user.play += 1
    user.rate = user.win / user.play * 100
    user.save()
    return Response()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userWin(request):
    user_id = request.data['pk']
    user = get_object_or_404(CustomUser, id=user_id)
    user.win += 1
    user.rate = user.win / user.play * 100
    user.save()
    return Response()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userInfo(request):
    user_id = request.data['pk']
    user = get_object_or_404(CustomUser, id=user_id)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userRank(request):
    user = CustomUser.objects.order_by('-rate')
    rank = []
    for i in range(5):
        ind = user[i].email.find('@')
        rank.append(user[i].email[:ind])
    return Response(rank)

# code 요청
def kakao_login(request):
    app_rest_api_key = '1959deb17d11d37e28fecfb81284c8c4'
    redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )    
    
# access token 요청
def kakao_callback(request):                                                                  
    params = urllib.parse.urlencode(request.GET)                                      
    return redirect(f'http://127.0.0.1:8000/accounts/login/kakao/callback?{params}')   