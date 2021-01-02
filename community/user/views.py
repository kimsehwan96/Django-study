from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password #DB에 암호화된 비밀번호가 저장됨. 필수
from .models import User
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다'
        else:
            user = User.objects.get(username=username) #username <- 클래스의 필드명 = username <-입력받은 변수
            if check_password(password, user.password):
                pass
                # 비밀번호 일치하는 부분
                # 세션처리 및 redirect 필요
            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'

        return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html') #뷰에서 담은 값들이 request 변수를 통해 전달
    elif request.method == 'POST':
        #html에 있는 name값으로 전달 받는다
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None) #html input tag name attr.
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not(username and password and re_password and useremail):  #예외처리
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )
            user.save()

        return render(request, 'register.html', res_data) # save()이후 다시 register.html 을 리턴했기때문에 가입 이후에도 이 페이지가 나옴
        #dict 형태로 메시지가 전달된다 -> context 전달개념