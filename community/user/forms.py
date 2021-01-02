from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자 이름") # template 안에 사용되는 Label name과 관련되어있다.
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호") # 템플릿에 전달된다 -> 인수들이
    ## widget=forms.인풋타입 -> templates에 widget type 결정
    