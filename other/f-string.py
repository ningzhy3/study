

def bar(func):
    def inner():
        print('in bar: before')
        func()
        print('in bar: end')
    return inner

@bar
def foo():
    print('foo!')

foo()