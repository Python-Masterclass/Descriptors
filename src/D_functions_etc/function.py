def f(x, y):
    print(f"{x=}, {y=}")


def main():
    p = f.__get__(1)
    p(3)


if __name__ == "__main__":
    main()
