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
    # part 1
    
    # part 2

if __name__ == "__main__":
    main()
