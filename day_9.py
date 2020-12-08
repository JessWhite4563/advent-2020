from generic import AdventRunner

class AdventDayNine(AdventRunner):

    def processData(self, file_data):
        return -1

advent = AdventDayNine()
advent.addData("./data/day-9/input.txt")
advent.additionalConfig = {'verbose': False}
print(advent.runScript())