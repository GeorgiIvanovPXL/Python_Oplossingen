def is_even(getal):
    if getal % 2 == 0:
        return True
    else:
        return False


def is_oneven(getal):
    if is_even(getal):
        return False
    else:
        return True


def main():
    print(is_oneven(5))


if __name__ == '__main__':
    main()
