from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from user.decorators import login_required
from .forms import RegisterForm
from .models import Order
# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product)) #에러 발생했을 경우 상품 상세보기로 리다이렉트

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update(
            {'request' : self.request}
        )

        return kw 

    ##부모 클래스의 get_form_kwargs를 호출하여 kw에 저장하고
    ## kw를 업데이트하는데 -> request를 넣어준다. (사용해되니까)

@method_decorator(login_required, name='dispatch') #실제 url 접근시 수행되는 메서드는 dispatch 이므러
class OrderList(ListView):
    # model = Order <- 모든 유저의 정보를 얻는 코드
    template_name = 'order.html'
    context_object_name = 'order_list'
    #TODO: 현재는 모든 유저의 주문 정보가 나온다
    #로그인한 사용자의 주문만 보기위해서는 queryset 을 이용해야하며
    #또 세션을 사용해야 한다.
    
    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email=self.request.session.get('user'))
        return queryset

        #이렇게 하면 로그인한 사용자의 주문 정보만 나온다
        #object.filter 내부의 user__email <- 이 구문이 어떻게 나온건지 좀 알아봐야것다

    # @login_required
    # def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
    #     return super().dispatch(request, *args, **kwargs)
    # 위처럼 하지 않아도 된다.