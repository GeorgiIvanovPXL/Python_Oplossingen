def print_formatting():
    for i in range(1, 15):
        print("{:3d} {:4d} {:5d}" .format(i, i * i, i * i * i))


def main():
    print_formatting()


if __name__ == '__main__':
    main()
