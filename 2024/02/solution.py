from operator import contains
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
    reports = read_input()
    reports = reports.splitlines()

    numSafe = 0
    numAlmostSafe = 0
    for i in range(len(reports)):

        reports[i] = reports[i].split(" ")
        deltaList = []
        unsafeDeltas = 0
        #ignore the start and the end elements, 
        for j in range(len(reports[i]) - 1):
            delta = int(reports[i][j]) - int(reports[i][j+1])

            if (delta == 0 or abs(delta) > 3):    
                unsafeDeltas +=1
                break

           
            if (len(deltaList)):
                prevDelta = deltaList[-1]

                # delta changed signs
                if ((prevDelta > 0 and delta < 0) or 
                    (prevDelta < 0 and delta > 0)):
                    unsafeDeltas +=1
                    break
        

            
            deltaList.append(delta)
        if (unsafeDeltas == 0):
            numSafe+=1
        if (unsafeDeltas <= 1):
            numAlmostSafe+=1

    print(numSafe)
    print(numAlmostSafe)

    # part 2

if __name__ == "__main__":
    main()
