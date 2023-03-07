class D:
    def __init__(self, msg):
        self.msg = msg

    def __get__(self, *args):
        return self.msg

    def __set__(self, *args):
        print(f"{self.msg}.__set__")


class R:
    def __init__(self, msg):
        self.msg = msg

    def __get__(self, *args):
        return self.msg


class A:
    s = "class A"

    d = D("descriptor A.d")

    def f(self):
        print("method A.f")


class B(A):
    s = "class B"

    d = R("descriptor B.d")

    def f(self):
        print("method B.f")

b = B()
b.s = "instance b"
