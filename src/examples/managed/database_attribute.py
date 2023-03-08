import sqlite3


class DatabaseAttribute:
    def __set_name__(self, owner, name):
        table = owner.__name__.lower()
        self.owner = owner
        self.fetch = f"SELECT {name} from {table} WHERE {owner.key}=?;"
        self.store = f"UPDATE {table} SET {name}=? WHERE {owner.key}=?;"

    def __get__(self, instance, owner_class=None):
        return self.owner.connection.execute(self.fetch, [instance.key]).fetchone()[0]

    def __set__(self, instance, value):
        self.owner.connection.execute(self.store, [value, instance.key])
        self.owner.connection.commit()


connection = sqlite3.connect("my_database.db")


class Table:
    def __init_subclass__(cls, **kwargs):
        conn = kwargs["connection"]
        cls.connection = conn
        table_name = cls.__name__.lower()
        fields = (
            field_name
            for field_name, instance in vars(cls).items()
            if isinstance(instance, DatabaseAttribute)
        )
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({cls.key} PRIMARY KEY, {', '.join(f for f in fields)});"
        conn.execute(sql)


class Item(Table, connection=connection):
    key = "id"
    name = DatabaseAttribute()
    price = DatabaseAttribute()

    def __init__(self, key, name=None, price=None):
        self.key = key
        self.connection.execute(
            f"INSERT INTO {self.__class__.__name__.lower()} ({self.__class__.key}) VALUES ({self.key});"
        )
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price


def main():
    item1 = Item(1, "book", 3.10)
    item2 = Item(2)
    print(f"{item1.name=}, {item1.price=}")
    print(f"{item2.name=}, {item2.price=}")
    item2.name = "DVD"
    item1.price = 5.99
    print(f"{item1.name=}, {item1.price=}")
    print(f"{item2.name=}, {item2.price=}")


if __name__ == "__main__":
    connection.execute("DELETE FROM item;")
    main()
