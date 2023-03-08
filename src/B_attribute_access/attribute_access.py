class Meta(type):
    def __getattribute__(cls, item):
        print(f"type.__getattribute__({cls}, {item})")
        return super().__getattribute__(item)
    
    def __setattr__(cls, key, value):
        print(f"type.__setattr__({cls}, {key}, {value})")
        return super().__setattr__(key, value)
    
    def __delattr__(cls, item):
        print(f"type.__delattr__({cls}, {item})")
        return super().__delattr__(item)
    
    x = 5


class A(metaclass=Meta):
    def __getattribute__(self, item):
        print(f"object.__getattribute__({self}, {item})")
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        print(f"object.__setattr__({self}, {key}, {value})")
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        print(f"object.__delattr__({self}, {item})")
        return super().__delattr__(item)

    x = 10


a = A()
a.__dict__["x"] = 15


if __name__ == "__main__":
    print(f"{a.x=}")
    a.x = 20
    del a.x
    print(f"{a.x=}")

    print(f"{A.x=}")
    A.x = 3
    del A.x
    print(f"{A.x=}")
