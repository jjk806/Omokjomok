from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage

import random

# Create your views here.
@api_view(['POST'])
def emailAuth(request):
    print(request.data)
    number = random.randrange(100000, 1000000)
    email = request.data['email'] # 받는 사람 이메일
    subject = '오목조목 회원 인증 메일' # 제목
    message = '인증하실 번호는' + str(number) + '입니다.' # 내용
    sendmail = EmailMessage(subject, message, to=[email])
    # EmailMessage(제목, 내용, 보내는 사람(settings 설정으로 안 적어도 됨), 받는 사람 목록)
    sendmail.send()
    return Response(number)