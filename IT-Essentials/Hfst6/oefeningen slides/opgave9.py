def vervang(tekst):
    real_text = tekst.replace('d', 'th').replace('cat', 'dog')
    print(real_text)


def main():

    tekst = "The quick brown fox jumps over de lazy cat."
    vervang(tekst)


if __name__ == '__main__':
    main()
