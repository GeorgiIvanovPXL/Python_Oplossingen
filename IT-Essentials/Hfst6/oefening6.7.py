import random


def encrypteer(tekst, random_getal):
    gëencrypteerd = ""
    for letter in tekst:
        gëencrypteerd += chr(ord(letter) + random_getal)

    return gëencrypteerd


def main():
    tekst = input("Geef een tekst in: ")
    getal = random.randint(2, 24)
    while getal % 2 != 0:
        getal = random.randint(2, 24)

    print(encrypteer(tekst, getal))


if __name__ == '__main__':
    main()
