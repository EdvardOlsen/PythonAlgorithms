from argparse import ArgumentParser


def second(arr):
    hachipuri = float("-inf")
    past_hachipuri = float("-inf")
    for num in arr:
        if num > hachipuri:
            past_hachipuri = hachipuri
            hachipuri = num
        elif num > past_hachipuri:
            past_hachipuri = num
    return past_hachipuri


def parse():
    parser = ArgumentParser()
    parser.add_argument("--a", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    hehe = parse()
    hehe = hehe.a.split(" ")
    hehe = [int(num) for num in hehe]
    print(second(hehe))
