def printx():
    print("x", end=" ")


def meerderex(aantal):
    for i in range(aantal):
        printx()


def main():
    meerderex(5)


if __name__ == '__main__':
    main()
