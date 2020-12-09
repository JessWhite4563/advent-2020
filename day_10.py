from generic import AdventRunner

class AdventDayTen(AdventRunner):

    def processData(self, file_data):
        return -1

advent = AdventDayTen()
advent.addData("./data/day-10/input.txt")
advent.additionalConfig = {'verbose': False}
print(advent.runScript())