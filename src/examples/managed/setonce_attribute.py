from weakref import WeakKeyDictionary


class SetOnce:
    def __init__(self):
        self.instance_value = WeakKeyDictionary()

    def __get__(self, instance, owner_class=None):
        return self.instance_value[instance]

    def __set__(self, instance, value):
        if instance in self.instance_value:
            raise AttributeError(f"Attribute can only be set once")
        self.instance_value[instance] = value


class C:
    x = SetOnce()


def main():
    c = C()
    d = C()
    print(list(C.__dict__["x"].instance_value.items()))
    c.x = "hello"
    d.x = "world"
    print(f"{c.x=}, {d.x=}")
    print(list(C.__dict__["x"].instance_value.items()))
    try:
        c.x = "bye"
    except AttributeError as e:
        print(e)
    print(f"{c.x=}, {d.x=}")
    print(list(C.__dict__["x"].instance_value.items()))
    del c
    print(list(C.__dict__["x"].instance_value.items()))


if __name__ == "__main__":
    main()
