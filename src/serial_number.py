from itertools import count


class SerialNumber:
    serial_number_generator = count(start=1)

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name
        setattr(owner, self.private_name, None)

    def __get__(self, obj, obj_type=None):
        value = getattr(obj, self.private_name, None)
        if value is None:
            value = next(self.serial_number_generator)
            setattr(obj, self.private_name, value)
        return value

    def __set__(self, obj, value):
        raise AttributeError()

    def __delete__(self, obj):
        raise AttributeError()


class A:
    sn = SerialNumber()


class B:
    part_number = SerialNumber()



class A:
    def __init__(self, v):
        self.value = v

    def f(self):
        return self.value
