def bereken_belasting(bedrag):
    belasting = 0
    if bedrag < 25000:
        belasting = bedrag * 0.384
    elif bedrag < 30000:
        belasting = (25000 * 0.384) + ((bedrag - 25000)* 0.50)
    else:
        belasting = (25000 * 0.384) + (5000 * 0.50) + ((bedrag - 30000) * 0.60)

    return belasting


def main():
    print(bereken_belasting(26500))


if __name__ == '__main__':
    main()