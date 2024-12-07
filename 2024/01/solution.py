import os

def read_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    try:
        with open(input_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
        return None

def main():
    print("Hello, World!")
    
    data = read_input()
    
    left = []
    right = []
    lines = data.splitlines()
    for line in lines:
        vals = line.split("  ")
        left.append(int(vals[0]))
        right.append(int(vals[1]))
    
    left.sort()
    right.sort()

    part1list = list(map(lambda val1, val2: abs( val1 - val2), left, right))
    
    dict = {}
    res = 0
    for entry in left:
        dict[entry] = right.count(entry)
        res += dict[entry] * entry


    print(res)
    # 23529853
   


    res = sum(part1list)
    print(res)
    # 1388114
    # print(part2res)

if __name__ == "__main__":
    main()
