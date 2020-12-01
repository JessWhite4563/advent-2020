from generic import AdventRunner


class AdventDayOne(AdventRunner):
    def __init__(self):
        self.additionalConfig = {}
        self.results = []
        super()

    def processData(self, file_data):
        print(self.additionalConfig)
        self.loopDepth(file_data, 0, self.additionalConfig['depth'])
        print(self.results)
        
        running = 1
        for num in self.results:
            running = running * num
        print(running)

    def loopDepth(self, file_data, value, depth):
        newDepth = depth - 1
        for row in file_data:
            if(row != ''):
                newValue = value + int(row)
                if (newDepth == 0):
                    if (newValue == self.additionalConfig['target']):
                        self.results.append(int(row))
                        return True
                else :
                    if(self.loopDepth(file_data, newValue, newDepth)):
                        self.results.append(int(row))
                        return True
        return False



advent = AdventDayOne()
advent.additionalConfig = {'depth': 3, 'target': 2020}
advent.runScript("C:/Users/Jessica/Documents/repos/advent/data/day-1/input.txt")
