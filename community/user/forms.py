from django import forms
from .models import User
from django.contrib.auth.hashers import check_password
class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={ #이렇게 커스텀 에러메세지 제작 가능
            'required' : "아이디를 입력해주세요" #이 키는 문서를 보고 확인
        },
        max_length=32, label="사용자 이름") # template 안에 사용되는 Label name과 관련되어있다.
    password = forms.CharField(
        error_messages={
            'required' : "비밀번호를 입력해주세요"
        },
        widget=forms.PasswordInput, label="비밀번호") # 템플릿에 전달된다 -> 인수들이
    ## widget=forms.인풋타입 -> templates에 widget type 결정
    
    #forms.Form의 clean 메서드를 확인해봐야겠네
    def clean(self):
        cleaned_data = super().clean() #기존 폼에있는 clean 함수 실행
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                self.add_error('username', '아이디가 없습니다.')
                return
                
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
                #상속받은 메서드 중 하나인 add error
            else:
                # 비밀번호 체크 완료되면
                self.user_id = user.id