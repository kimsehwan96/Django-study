from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password #DB에 암호화된 비밀번호가 저장됨. 필수
from django.views.decorators.http import require_http_methods #Http Method를 강제하기 위한(허용된 메서드만 허용)
from .models import User
from .forms import LoginForm
# Create your views here.

def home(request):
    user_id = request.session.get('user') ##login에서 request.session['user']에 user.id 를 넣어줬기 때문
    #세션 처리 로직
    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse(user.username)
    return HttpResponse('Home')

def logout(request):
    #로그아웃은 그냥 세션에 있는 값을 날리면 되것지
    if request.session.get('user'):#session있으면
        del(request.session['user'])

    return redirect('/')



# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)

#         res_data = {}

#         if not (username and password):
#             res_data['error'] = '모든 값을 입력해야합니다'
#         else:
#             user = User.objects.get(username=username) #username <- 클래스의 필드명 = username <-입력받은 변수
#             if check_password(password, user.password):
#                 request.session['user'] = user.id #session의 user에 user.id를 넣어준다.
#                 return redirect('/') #redirect할 url 작성
#                 # 비밀번호 일치하는 부분
#                 # 세션처리 및 redirect 필요
#             else:
#                 res_data['error'] = '비밀번호를 틀렸습니다.'

#         return render(request, 'login.html', res_data)

@require_http_methods(['GET', 'POST']) #이 데코레이터가 있으면 GET, POST 메서드만 허용
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) #POST에 있는 데이터가 form에 들어감
        if form.is_valid(): #form 인스턴스는 is_vaild 갖고있다.
            #두개의 값을 모두 입력하면(폼클래스에) 밑에 리턴 코드 실행
            #유효하지 않으면 폼안에 에러정보가 들어간다.
            #값이 들어있는지 아닌지만 판단한다.
            #우리가 직접 폼 클래스에 오버라이드해서 작성
            request.session['user'] = form.user_id #form에 self.user_id = user.id 로 받아옴
            return redirect('/') #정상이면 리다이렉트
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})


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