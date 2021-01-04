from django import forms
from .models import Board

class BoardForm(forms.Form):

    title = forms.CharField(
        error_messages={ #이렇게 커스텀 에러메세지 제작 가능
            'required' : "제목을 입력해주세요" #이 키는 문서를 보고 확인
        },
        max_length=128, label="제목") # template 안에 사용되는 Label name과 관련되어있다.
        
    contents = forms.CharField(
        error_messages={
            'required' : "내용을 입력해주세요"
        },
        widget=forms.Textarea, label="내용") # 템플릿에 전달된다 -> 인수들이
    ## widget=forms.인풋타입 -> templates에 widget type 결정
