import logging


class Choice:
    def __init__(self, *args):
        self.options = args

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner_class=None):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value not in self.options:
            raise ValueError(f"Invalid value '{value}'. Expected one of {self.options}")
        setattr(instance, self.private_name, value)


class C:
    color = Choice("red", "black")


def main():
    c = C()
    c.color = "red"
    print(c.color)
    try:
        c.color = "green"
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
