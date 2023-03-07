from src.examples.choice import Choice


class NumberWithUnit(float):
    def __new__(cls, value, unit):
        return super().__new__(cls, value)

    def __init__(self, value, unit):
        self.unit = unit

    def __str__(self):
        return f"{super().__str__()} {self.unit}"


class Temperature:
    to_kelvin = {
        "K": lambda x: x,
        "C": lambda x: x + 273.15,
        "F": lambda x: (x - 32)/1.8 + 273.15,
    }

    from_kelvin = {
        "K": lambda x: x,
        "C": lambda x: x - 273.15,
        "F": lambda x: (x - 273.15) * 1.8 + 32
    }

    unit = Choice("K", "C", "F")

    def __init__(self, unit="K"):
        self.unit = unit

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner_class):
        temp_in_kelvin = getattr(instance, self.private_name)
        return NumberWithUnit(self.from_kelvin[self.unit](temp_in_kelvin), self.unit)

    def __set__(self, instance, value):
        temp_in_kelvin = self.to_kelvin[self.unit](value)
        setattr(instance, self.private_name, temp_in_kelvin)

    def __str__(self):
        pass

class C:
    t = Temperature()


def main():
    c = C()
    c.t = 273.15
    print(c.t)
    c.t.unit = "C"
    print(c.t.unit)
    print(c.t)


if __name__ == "__main__":
    main()
