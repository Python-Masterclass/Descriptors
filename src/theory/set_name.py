class ClassWithSetName:
    def __init__(self):
        print(f"{self.__class__.__name__}: initialization")

    def __set_name__(self, owner, name):
        print(f"{self.__class__.__name__}: __set_name__({owner}, {name})")
        self.owner = owner
        self.name = name


class Descriptor(ClassWithSetName):
    def __get__(self, instance, owner_class):
        print(f"{self.__class__.__name__}: __get__({instance}, {owner_class}")
        print(f"{self.owner=}, {self.name=}")
        return 42


class C:
    non_descriptor = ClassWithSetName()
    descriptor = Descriptor()


if __name__ == "__main__":
    c = C()
    print(f"{c.descriptor=}")
    print(f"{C.descriptor=}")
