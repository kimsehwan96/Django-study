#데코레이터 함수 작성
from django.shortcuts import redirect
from user.models import User

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs) #이렇게 리턴하는 함수에도 똑같이 인자를 모두 전달해준다
    return wrap

# oder.views 에서 OrderList에 해당 데코레이터를 넣었을때 에러 발생하는 이유
# OrderList의 메서드인 dispatch를 랩핑하려고 하는데
# OrderList.dispatch 메서드의 프로토타입은 다음과 같음
# def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse
# 인자에 request가 들어간다!


def admin_required(function): #유저 등급이 admin이 아닌경우 홈으로 보내버리는 데코레이터
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        user = User.objects.get(email=user)
        #유저 객체를 찾을 수 있다.
        if user.level != 'admin':
            return redirect('/')
        return function(request, *args, **kwargs) #이렇게 리턴하는 함수에도 똑같이 인자를 모두 전달해준다
    return wrap

# 관리자만 들어가야하는 페이지의 경우 admin_required 데코레이터를 이용하면 매우 간단!

