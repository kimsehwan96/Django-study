# Decorator

- 함수를 Wrapping 
- 기능의 재사용

```python3

def test_func():
    if user is None:
        return redirect('/login')
    print("Do something")


def test_func2():
    if user is None:
        return redirect('/login')
    print("Do something2")

#위와같이 동일한 로직이 계속 함수 중간에 들어간다?

```

## 다음과 같이 수정 가능

```python3

def login_required(func):
    def wrap():
        if user is None:
            return redirect('login')
        return func() #데코레이터 밑에 들어오는 함수를 실핼ㅇ
    return wrap() #wrap 함수를 수행하며, wrap함수에 적혀있는 로직을 수행한 이후 인자로 들어온 함수의 로직또한 수행


@login_required
def test_func():
    print("Do something")

@login_required
def test_func2():
    print("Do something2")

```

