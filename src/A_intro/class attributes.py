class Meta(type):
    x = 3


class M(Meta):
    pass


class A(metaclass=M):
    pass


class B(A):
    pass


def main_1():
    print(A.x)
    print(Meta.x)
    try:
        print(A.y)
    except AttributeError as e:
        print(f"{e.__class__.__name__}: {e}")


def main_2():
    print(B.x)
    print(M.x)


def main_3():
    A.x = 5
    try:
        print(B.__dict__["x"])
    except KeyError as e:
        print(f"{e.__class__.__name__}: {e}")
    print(B.x)
    print(M.x)


def main_4():
    A.x = 5
    del A.x
    print(B.x)
    print(M.x)


def main_5():
    A.x = 5
    try:
        del B.x
    except AttributeError as e:
        print(f"{e.__class__.__name__}: {e}")
    print(B.x)
    print(M.x)


if __name__ == "__main__":
    print("### 1 ###")
    main_1()
    print("### 2 ###")
    main_2()
    print("### 3 ###")
    main_3()
    print("### 4 ###")
    main_4()
    print("### 5 ###")
    main_5()
