import math


def get_length(vec: tuple) -> float:
    return math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2) + math.pow(vec[2], 2))


def main():
    print(get_length((-0.98, 3.41, -1.53)))


main()
