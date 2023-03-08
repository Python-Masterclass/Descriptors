class InstanceAttribute:
    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name
        self.hidden_name = "_" + name

    def __get__(self, instance, owner_class=None):
        return getattr(instance, self.hidden_name)

    def __set__(self, instance, value):
        setattr(instance, self.hidden_name, value)

    def __delete__(self, instance):
        delattr(instance, self.hidden_name)


class C:
    x = InstanceAttribute()


def main():
    c = C()
    print(c.__dict__)
    c.x = "hallo"
    print(c.__dict__)
    print(c.x)
    del c.x
    print(c.__dict__)


if __name__ == "__main__":
    main()
