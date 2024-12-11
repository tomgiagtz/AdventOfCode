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


MAS = "MAS"

diags = [
    [1, 1],
    [-1, 1],
    [-1, -1],
    [1, -1]
]


def searchForMas(array, center):
    if center[0] - 1 < 0 or center[0] + 1 >= len(array):
        return 0
    elif center[1] - 1 < 0 or center[1] + 1 >= len(array[center[0]]):
        return 0
    goodDiags = 0
    for i, diag in enumerate([[1, 1], [-1, 1]]):
        val = array[center[0] + diag[0]][center[1] + diag[1]]
        if not (val == "M" or val == "S"):
            return 0
        otherSide = diags[(i + 2) % 4]
        otherVal = array[center[0] + otherSide[0]][center[1] + otherSide[1]]
        if val == "M" and otherVal == "S":
            goodDiags += 1
        if val == "S" and otherVal == "M":
            goodDiags += 1

    #
    return goodDiags == 2


def main():
    input = read_input()
    array = input.splitlines()
    array = [list(i) for i in array]

    # part 1
    dispArray = copy.deepcopy(array)
    totalXmas = 0

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'X':
                numHits = searchForXmas(array, [i, j])
                if numHits > 0:
                    # dispArray[i][j] = str(numHits)
                    totalXmas += numHits
        # print("checked row " + "".join(array[i]))

    print(totalXmas)

    # part 2
    totalMas = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'A':
                numHits = searchForMas(array, [i, j])
                if numHits > 0:
                    # dispArray[i][j] = str(numHits)
                    totalMas += numHits

    print(totalMas)


if __name__ == "__main__":
    main()
