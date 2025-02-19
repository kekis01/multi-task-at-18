from hashlib import md5
from random import choice
import concurrent.futures


def coin_generator(zero):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("0000"):
            return f"{s} {h}"


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=61) as executor:
        for coin in zip(executor.map(coin_generator, "0000")):
            print(coin)


if __name__ == '__main__':
    main()

