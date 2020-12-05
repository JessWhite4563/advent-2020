from generic import AdventRunner

class AdventDayTemplate(AdventRunner):

    def processData(self, file_data):
        return -1

advent = AdventDayTemplate()
advent.addData("./data/day-1/input.txt")
advent.additionalConfig = {'verbose': False}
print(advent.runScript())