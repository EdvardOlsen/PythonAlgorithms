from argparse import ArgumentParser

def sum_list(arr):
    hachipuri = 0
    for num in arr:
        if num%2 == 0:
            hachipuri += num
    return hachipuri

def parse():
    parser = ArgumentParser()
    parser.add_argument('--a', type=str)
    return parser.parse_args()


if __name__ == '__main__':
    hehe = parse()
    hehe = hehe.a.split(' ')
    hehe = [int(num) for num in hehe]
    print(sum_list(hehe))