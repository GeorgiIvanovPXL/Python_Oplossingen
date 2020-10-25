import random


def print_random_getal():
    rand_getal = random.randint(-200, 1000)
    while str(rand_getal)[len(str(rand_getal)) - 1] != "0":
        rand_getal = random.randint(-200, 1000)

    print(rand_getal)


def main():
    print_random_getal()


if __name__ == '__main__':
    main()
