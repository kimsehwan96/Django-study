from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm
# Create your views here.


class ProductList(ListView):
    model = Product #원래는 이게 끝임.
    template_name = 'product.html'
    #default로 전달되는 context 이름이 object_list인데. 변경 가능
    context_object_name = "product_list" #이게 더 나은듯.

class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()#쿼리셋 정의 가능
    #queryset = Product.objects <- 이부분에 필터를 걸 수 있다.
    context_object_name = 'product' #컨텍스트명 명시하기
    #self.request가 존재한다.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #이미 생성된 context_data를 받아와서 수정해서 다시 return함다
        #그니까 이미있는 context에 우리가 커스템해서 뭔가 우겨넣기 위한 용도.
        context['form'] = OrderForm(self.request) #이 폼은 생성자를 재정의하였다(request를 전달 받을 수 있도록) request를 받아야 세션 처리가 가능해서


        return context