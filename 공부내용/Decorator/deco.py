def deco_test(func):
    def wrap():
        print("this is wrapper function !")
        return func()
    return wrap()

@deco_test
def func_test():
    print("I'm func_test !")

def test():
    print("Hi")

def func_arg(func):
    return func()

func_arg(test)