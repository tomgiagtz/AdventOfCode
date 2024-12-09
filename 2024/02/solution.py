from operator import contains
import os


class ReportInfo:
    levels = []
    deltas = []
    isSafeDeltas = []
    numSafe = 0
    numNotSafe = 0

    def __repr__(self):
        return (f"\nSafe: {self.numSafe}, Not Safe: {self.numNotSafe}\n"
                f"Levels: {self.levels}\n"
                f"Deltas: {self.deltas}\n"
                f"Is Safe Deltas: {self.isSafeDeltas}")


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

    # list of Dampenable Reports
    unsafeReports = []
    unsafeReportDeltas = []
    for i in range(len(reports)):
        # for each report
        reportInfo = ReportInfo()

        # split each line into an array
        currReportLevels = list(map(lambda x: int(x), reports[i].split(" ")))

        reportInfo.levels = currReportLevels

        # list of deltas
        deltaList = []
        # list of whether each delta is safe
        deltaIsSafeList = []
        unsafeDeltas = 0

        # ignore the end element, for checking j+1
        for j in range(len(currReportLevels) - 1):
            # for each delta
            delta = int(currReportLevels[j]) - int(currReportLevels[j + 1])
            isDeltaSafe = True
            if delta == 0 or abs(delta) > 3:
                unsafeDeltas += 1
                isDeltaSafe = False

            # not first delta
            elif len(deltaList):
                prevDelta = deltaList[-1]

                # delta changed signs
                if ((prevDelta > 0 and delta < 0) or
                        (prevDelta < 0 and delta > 0)):
                    unsafeDeltas += 1
                    isDeltaSafe = False

            deltaList.append(delta)
            deltaIsSafeList.append(isDeltaSafe)

        if unsafeDeltas == 0:
            numSafe += 1
            numAlmostSafe += 1

        elif unsafeDeltas <= 2:
            reportInfo.deltas = deltaList
            reportInfo.isSafeDeltas = deltaIsSafeList
            reportInfo.numSafe = len(deltaList) - unsafeDeltas
            reportInfo.numNotSafe = unsafeDeltas

            unsafeReports.append(reportInfo)
            numAlmostSafe += 1

    print(numSafe)
    print(numAlmostSafe)

    # part 2
    for report in unsafeReports:
        print(report)


if __name__ == "__main__":
    main()
