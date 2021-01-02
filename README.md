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

