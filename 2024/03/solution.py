import os
import re


def read_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    try:
        with open(input_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
        return None


def main():
    print("Hello, World!")
    # part 1
    input = read_input()
    print(input)
    instructions = re.findall(r"mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don't\(\)", input)

    # mulPairs = [match.replace('mul(', '').replace(')', '').split(',') for match in matches if match[0] == 'm']
    # print(mulPairs)
    # mulPairs = [list(map(int, pair)) for pair in mulPairs if pair[0] != 'd']
    # # dodont = re.findall(r"do\(\)|don't\(\)", input)
    isEnabled = True
    res = 0
    for instruction in instructions:
        if instruction[0] == 'm' and isEnabled:
            mulPair = instruction.replace('mul(', '').replace(')', '').split(',')
            res += int(mulPair[0]) * int(mulPair[1])
        elif instruction == 'do()':
            isEnabled = True
        elif instruction == 'don\'t()':
            isEnabled = False

    # part 2
    print(res)


if __name__ == "__main__":
    main()
