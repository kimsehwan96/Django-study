from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.


class ProductList(ListView):
    model = Product #원래는 이게 끝임.
    template_name = 'product.html'
    #default로 전달되는 context 이름이 object_list인데. 변경 가능
    context_object_name = "product_list" #이게 더 나은듯.
    