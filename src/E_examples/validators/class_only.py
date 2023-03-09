class ClassOnlyMethod(classmethod):
    def __get__(self, instance, cls=None):
        if instance is not None:
            raise AttributeError("You fool")
        return super().__get__(instance, cls)


class C:
    @ClassOnlyMethod
    def f(cls):
        print("Yeah")


def main():
    c = C()
    C.f()
    try:
        c.f()
    except Exception as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    main()
