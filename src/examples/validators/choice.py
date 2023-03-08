from src.examples.managed.instance_attribute import InstanceAttribute
from src.examples.validators.validator import Validator


class Choice(Validator, InstanceAttribute):
    def __init__(self, *values, **kwargs):
        self.values = values
        super().__init__(**kwargs)

    def validate(self, value):
        if value not in self.values:
            raise ValueError(f"Invalid value '{value}'. Expected one of {self.values}")


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
