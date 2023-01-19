def multiple_args(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    multiple_args(test=5, name="bob", age=20)
