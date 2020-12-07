from generic import AdventRunner

class AdventDayEight(AdventRunner):

    def processData(self, file_data):
        return -1

advent = AdventDayEight()
advent.addData("./data/day-8/input.txt")
advent.additionalConfig = {'verbose': False}
print(advent.runScript())