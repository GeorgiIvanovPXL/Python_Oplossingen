def get_tienden(decimaal):
    tekst = str(decimaal)
    lijst = str.split(tekst, '.')
    return lijst[1][0]


def main():
    print(get_tienden("45.235"))


if __name__ == '__main__':
    main()
