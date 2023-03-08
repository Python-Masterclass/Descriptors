class A:
    x = 3


class B(A):
    pass


def main_1():
    a = A()
    print(a.x)
    print(A.x)
    try:
        print(a.y)
    except AttributeError as e:
        print(f"{e.__class__.__name__}: {e}")



def main_2():
    b = B()
    print(b.x)
    print(B.x)


def main_3():
    b = B()
    b.x = 5
    print(b.x)
    print(B.x)


def main_4():
    b = B()
    b.x = 5
    del b.x
    print(b.x)
    print(B.x)


def main_5():
    b = B()
    try:
        del b.x
    except AttributeError as e:
        print(f"{e.__class__.__name__}: {e}")
    print(b.x)
    print(B.x)


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
