def foo(a, b, c):
    print(a, b, c)


def goo(*args, **kwargs):
    print(kwargs)
    foo(*args, **kwargs)


goo(22, b=3, c=6)
