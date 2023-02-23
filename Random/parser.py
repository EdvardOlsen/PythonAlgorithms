from argparse import ArgumentParser
def parse():
    parser = ArgumentParser()
    parser.add_argument('--a', type=int)
    parser.add_argument('--b', type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse()
    print(args)