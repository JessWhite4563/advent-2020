from generic import AdventRunner

class AdventDayTemplate(AdventRunner):

    def processData(self, file_data):
        start_list = file_data[0].split(',')
        previous = {}
        last = 0
        for i in range(0, self.additionalConfig['target']):
            if i < len(start_list):
                val = int(start_list[i])
                if i > 0:
                    previous[last] = i-1
                last = val
            else:
                if last in previous.keys():
                    val = (i-1) - previous[last]
                    previous[last] = i-1
                    last = val
                else:
                    val = 0
                    previous[last] = i-1
                    last = val

            self.outputDebug('said %i'% val)

        return val

advent = AdventDayTemplate()
advent.addData("./data/day-15/input.txt")

advent.additionalConfig = {'verbose': False, 'target':2020}
print('Part 1 = %i' % advent.runScript())
advent.additionalConfig = {'verbose': False, 'target':30000000}
print('Part 2 = %i' % advent.runScript())