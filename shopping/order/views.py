from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from .forms import RegisterForm
# Create your views here.

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