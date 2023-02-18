import argparse
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, required=True, help='Path to input file.')


if __name__ == '__main__':
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        lines = f.readlines()

    elves = []

    accumulator = 0
    for line in lines:
        if line == '\n':
            elves.append(accumulator)
            accumulator = 0
        else:
            accumulator += int(line)

    pprint(elves)
    print(f'Max: {max(elves)}')
