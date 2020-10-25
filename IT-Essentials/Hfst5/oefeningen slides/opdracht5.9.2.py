import random


def genereer_getallen():
    for i in range(10):
        print(
            random.randint(0, 10))


def main():

    genereer_getallen()


if __name__ == '__main__':
    main()
