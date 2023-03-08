import logging

logging.basicConfig(level=logging.INFO)


class LoggedAccess:
    def __set_name__(self, owner, name):
        self.attr_name = name
        self.hidden_name = "_" + name

    def __get__(self, instance, owner_class=None):
        value = getattr(instance, self.hidden_name)
        logging.info(f"Accessing {self.attr_name} of {type(instance).__name__} object, value = {value}")
        return value

    def __set__(self, instance, value):
        logging.info(f"Setting {self.attr_name} of {type(instance).__name__} object to {value}")
        setattr(instance, self.hidden_name, value)


class C:
    x = LoggedAccess()


def main():
    c = C()
    c.x = 3
    print(c.x)


if __name__ == "__main__":
    main()
