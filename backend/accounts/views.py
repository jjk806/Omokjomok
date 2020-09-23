from django.shortcuts import render
from rest_framework.response import Response
from django.core.mail import EmailMessage

import random

# Create your views here.
def emailAuth(request):
    emailTo = request.data.email
    number = random.randrange(100000, 1000000)
    email = EmailMessage(
        '오목조목 회원 인증 메일', # 제목
        '인증하실 번호는' + str(number) + '입니다.', # 내용
        # '', # 보내는 이메일(settings에서 설정해서 작성안해도 됨)
        to=[emailTo] # 받는 이메일 목록
    )
    email.send()
    return Response(number)