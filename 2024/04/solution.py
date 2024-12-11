import os
import copy

WORDLENGTH = 4
XMAS = "XMAS"


def print2DArray(array):
    for i in range(len(array)):
        print("".join(array[i]))


def read_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    try:
        with open(input_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
        return None


dirMap = [
    [-1, 0],  # up
    [1, 0],  # down
    [0, -1],  # left
    [0, 1],  # right
    [-1, -1],  # upLeft
    [-1, 1],  # upRight
    [1, -1],  # downLeft
    [1, 1]  # downRight
]


def searchForXmas(array, center):
    numHits = 0
    possibleDirs = []
    for direction in dirMap:

        if center[0] + (direction[0] * (len(XMAS) - 1)) < 0:
            # print("top too close")
            continue
        elif center[0] + (direction[0] * (len(XMAS) - 1)) >= len(array):
            # print("bottom too close")
            continue
        elif center[1] + (direction[1] * (len(XMAS) - 1)) < 0:
            # print("left too close")
            continue
        elif center[1] + (direction[1] * (len(XMAS) - 1)) >= len(array[0]):
            # print("right too close")
            continue
        possibleDirs.append(direction)

    # print(possibleDirs)
    for dir in possibleDirs:
        isXmas = True
        for i in range(len(XMAS)):
            if array[center[0] + dir[0] * i][center[1] + dir[1] * i] != XMAS[i]:
                isXmas = False
                break
        if isXmas:
            # print(f"found {XMAS} at {center} w dir {dir}")
            numHits += 1

    # print(numHits)
    return numHits


def main():
    input = read_input()
    array = input.splitlines()

    array = [list(i) for i in array]
    dispArray = copy.deepcopy(array)
    totalXmas = 0
    # print2DArray(array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'X':
                numHits = searchForXmas(array, [i, j])
                if numHits > 0:
                    # dispArray[i][j] = str(numHits)
                    totalXmas += numHits
        # print("checked row " + "".join(array[i]))

    # print2DArray(dispArray)
    print(totalXmas)


if __name__ == "__main__":
    main()
