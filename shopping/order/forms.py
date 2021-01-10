from django import forms
from .models import Order
from product.models import Product
from user.models import User
from django.db import transaction #트랜잭션을 위해서

class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        res =super().__init__(*args, **kwargs) #부모 클래스의 생성자 상속 및 호출
        self.request = request # 이 폼을 생성하는 곳에서 request가 있으니, request를 전달받아야겠지? ->request는 views.py에.
        
    quantity = forms.IntegerField(
        error_messages={
            'required' : '수량을 입력해주세요.'
        },
        label='수량'
    )

    product = forms.IntegerField( #DB의 숫자로된 id를 자동으로 받아올거라서 입력 필요 없음
        error_messages={
            'required' : '상품명을 입력해주세요.'
        }, label='상품 설명', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data =super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user') #이렇게 form에는 request가 없지만 생성자에 명시하고
        #form을 생성하는 view에서 request 인자를 전달해주면 가능하다. 
        

        if quantity and product and user:
            with transaction.atomic(): #원자적
                prod = Product.objects.get(pk=product)
                order = Order(
                    quantity=quantity,
                    product=prod,
                    user=User.objects.get(email=user)
                )
                order.save() #실제 이러한 주문을 저장하기.
                prod.stock -= quantity #재고를 quantity만큼 제거.
                prod.save() #주문정보 저장 이후 product의 재고 정보도 저장
            
            #transaction.atomic()안에서 실행할경우 원자적으로 차리됨.
            #실제 테스트 결과 원자적 수행 잘 된다.
            # ->transaction & atomic 연산에 대해서 좀 더 알아보기 !!
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')
