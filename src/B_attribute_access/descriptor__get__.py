import logging


class NonDataDescriptor:
    def __init__(self, value):
        self.value = value

    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name

    def __get__(self, instance, owner_cls=None):
        print(f"{self.__class__.__name__}: {self.owner.__name__}.{self.name}.__get__({instance}, {owner_cls})")
        return self.value


class DataDescriptor(NonDataDescriptor):
    def __set__(self, instance, value):
        print(f"{self.__class__.__name__}: {self.owner.__name__}.{self.name}.__set__({instance}, {value})")

    def __delete__(self, instance):
        print(f"{self.__class__.__name__}: {self.owner.__name__}.{self.name}.__delete__({instance})")


class Meta(type):
    a = NonDataDescriptor("Meta-a")
    b = DataDescriptor("Meta-b")


class A(metaclass=Meta):
    x = NonDataDescriptor(10)
    y = DataDescriptor(20)
    a = "class-a"
    b = "class-b"


a = A()
a.__dict__["x"] = "hello"
a.__dict__["y"] = "world"


def main_1():
    print("Getting a.x")
    print(f"{a.x=}")
    print("\nGetting a.y")
    print(f"{a.y=}")
    print("\nGetting A.x")
    print(f"{A.x=}")
    print("\nGetting A.y")
    print(f"{A.y=}")
    print("\nGetting A.a")
    print(f"{A.a=}")
    print("\nGetting A.b")
    print(f"{A.b=}")
    print("\nDeleting A.a and getting A.a")
    del A.a
    print(f"{A.a=}")


if __name__ == "__main__":
    main_1()
