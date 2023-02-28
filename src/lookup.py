class DD:
    def __get__(self, obj, owner=None):
        print(f"DD.__get__({obj=}, {owner=})")
        return self

    def __set__(self, obj, value):
        print(f"DD.__set__({obj=}, {value=})")

    def __delete__(self, obj):
        print(f"DD.__delete__({obj=})")


class NDD:
    def __get__(self, obj, owner=None):
        print(f"NDD.__get__({obj=}, {owner=})")
        return self


class WOD:
    def __set__(self, obj, value):
        print(f"WOD.__set__({obj=}, {value=})")

    def __delete__(self, obj):
        print(f"WOD.__delete__({obj=})")


class A:
    x = DD()
    y = NDD()
    z = WOD()


def set_main():
    a = A()
    a.__dict__["x"] = 40
    a.__dict__["y"] = 50
    a.__dict__["z"] = 60
    a.x = 4
    a.y = 5
    a.z = 6
    print()
    print(f"{a.x=}")
    print(f"{a.y=}")
    print(f"{a.z=}")
    print(f"{A.x=}, {A.y=}, {A.z=}")


def del_main():
    a = A()
    a.__dict__["x"] = 4
    a.__dict__["y"] = 5
    a.__dict__["z"] = 6
    del a.x
    del a.y
    del a.z
    print()
    print(f"{a.x=}")
    print(f"{a.y=}")
    print(f"{a.z=}")


def get_main():
    a = A()
    a.__dict__["x"] = 4
    a.__dict__["y"] = 5
    a.__dict__["z"] = 6
    print()
    print(f"{a.x=}")
    print(f"{a.y=}")
    print(f"{a.z=}")


if __name__ == "__main__":
    set_main()
