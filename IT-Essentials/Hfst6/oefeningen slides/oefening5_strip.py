def strip():
    print("*"+"      dit is een test \n " .strip() + "*")
    pxl_url = "www.pxl.be"

    return pxl_url.strip("w.be")


def main():
    strip()
    print(strip())


if __name__ == '__main__':
    main()

