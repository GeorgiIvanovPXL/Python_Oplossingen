def check_jaar(jaartal):
    if jaartal % 4 == 0 and jaartal % 100 != 0:
        return True
    elif jaartal % 400 == 0:
        return True
    else:
        return False


def main():
    print(check_jaar(2002))


if __name__ == '__main__':
    main()
