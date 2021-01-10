from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
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
    