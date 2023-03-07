import logging


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
    except AttributeError:
        logging.exception("")



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
    except AttributeError:
        logging.exception("")
    print(b.x)
    print(B.x)


if __name__ == "__main__":
    main_1()
