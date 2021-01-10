#데코레이터 함수 작성
from django.shortcuts import redirect

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