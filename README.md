# 파이썬 웹프레임워크인 django를 파헤쳐보자


## MVC 패턴?

- 디자인 패턴 중 하나이며 MVC는 다음의 약자이다.
    - Model 
    - View
    - Contorller 

- 사용자가 Controller를 조작하면, Contorller는 model을 통해 데이터을 가져오고
- 그 정보를 바탕으로 View를 제어하여 사용자에게 전달한다.

## 모델
- 애플리케이션의 정보, 데이터를 타나낸다.
- 데이터베이스, 상수, 초기화값 변수 등등.
- 모델은 다음과 같은 규칙을 가진다.
    - 사용자가 편집하길 원하는 모든 데이터을 가지고 있어야 한다.
    - 뷰나 컨트롤러에 대해 어떤 정보도 알지 말아야 한다.
    - 변경이 일어나면 변경 통지에 대한 처리 방법을 구현해야 한다.

## 뷰
- 사용자 인터페이스 요소를 의미하며, 다음과 같은 규칙들이 있다.
    - 모델이 가지고 있는 정보를 따로 저장해서는 안된다.
    - 모델이나 컨트롤러와 같이 다른 구성요소들을 몰라야 된다.
    - 변경이 일어나면 변경통지에 대한 처리방법을 구현해야만 한다.

## 컨트롤러
- 모델이나 뷰에 대해서 알고 있어야 한다
- 모델이나 뷰의 변경을 모니터링 해야 한다.


## Django start!!

- `django-admin startproject 프로젝트명`
- `cd 프로젝트명`
- `django-admin startapp 앱이름`


## Djnago는?
- Model
- View
- Template

### app 내부 모델 DB migration!

- app의 models.py에 클래스 정의 이후
- 프로젝트의 settings.py에서 Installed App에 등록한다.
- 이후 BACKEND 설정을 하고 (mysql, oracle, postgresql....)
- python3 manage.py makemigrations && python3 manage.py migrate

- id는 자동으로 생성되며, auto increament 



## community
- 장고를 이용하여 기본적인 회원가입, 글쓰기, 태그 관리 구현 (CRUD 모두 구현하진 않음), + 세션처리

## 두번쨰 프로젝트 (간단한 쇼핑몰 앱)
- 클래스를 활용한 뷰 생성
    - 클래스는 재사용이 용이하다.

#### 1일차
- `product`, `order`, `user`라는 세 앱을 생성, 세 앱에 모델을 작성하고 `makemigration` 과 `migrate` 진행

- 각 모델을 작성할때 배운점
- Meta 클래스는 관리자 모드에서 편하게 사용하기 위해 작성하며
    - DB table 이름을 명시해서 생성 가능
    
```python3
from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(
        verbose_name="이메일"
    )
    password = models.CharField(max_length=64,
        verbose_name="비밀번호"
    )
    registered_data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="사용자 등록 날짜"
    )

    class Meta:
        db_table = 'shopping_user'
        verbose_name = '유저'
        verbose_name_plural = "유저"
```

- 위 모델 코드를 보면 email은 models.EmailField 를 사용.
- Meta클래스에 테이블 이름 명시

```python3
from django.db import models

# Create your models here.
class Order(models.Model):
    #주문한 사용자
    user = models.ForeignKey(
        'user.User', #앱 안에있는 모델을 지정
        on_delete=models.CASCADE,
        verbose_name="사용자"
        )
    product = models.ForeignKey(
        'product.Product', 
        on_delete=models.CASCADE,
        verbose_name="상품"
        )
    quantity = models.IntegerField(
        verbose_name="수량"
        )
    registered_data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="등록 날짜"
        )

    class Meta:
        db_table = 'shopping_order'
        verbose_name = '주문'
        verbose_name_plural = "주문"

```

- 위 코드는 주문에 대한 객체 모델링이였음
- 유저와 프로덕트는 외래키로 사용함. `앱이름.모델명` 을 `ForeignKey` 메서드의 첫번째 인자로 넣어주어야 함.
    - `models.ForeignKey(모델명, on_delete=외래키삭제시동작)`

- `python3 manage.py makemigration && python3 manage.py migrate` 사용시 주의사항
    - 우선 `settings.py` 에 데이터베이스 생성되어있는지 확인
    - INSTALLED_APP에 앱들이 등록되었는지 확인

```SQL
CREATE DATABASE shopping_app default CHARACTER SET UTF8;
```

- DB생성 SQL이다. 주의점 default CHARSET을 UTF8로 명시하여 생성해야함!

** 1일차 끝 **

