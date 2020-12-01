from generic import AdventRunner
import copy

class AdventDayOne(AdventRunner):
    def __init__(self):
        super()
        self.results = []

    def processData(self, file_data):
        self.loopDepth(file_data, 0, self.additionalConfig['depth'], [])
        print('output: ' + str(self.results))
        
        running = 1
        for num in self.results:
            running = running * num
        print('result: ' + str(running))

    def loopDepth(self, file_data, value, depth, selected):
        newDepth = depth - 1
        for row in file_data:
            if row != '' and value < self.additionalConfig['target']:
                num = int(row)
                if num not in selected:
                    newValue = value + num
                    if newDepth == 0:
                        if newValue == self.additionalConfig['target']:
                            self.results.append(num)
                            return True
                    else :
                        newSelected = copy.copy(selected)
                        newSelected.append(num)
                        if self.loopDepth(file_data, newValue, newDepth, newSelected):
                            self.results.append(num)
                            return True
        return False

advent = AdventDayOne()
advent.additionalConfig = {'depth': 3, 'target': 2020}
advent.runScript("./data/day-1/input.txt")
