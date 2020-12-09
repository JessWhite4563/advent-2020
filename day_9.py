from generic import AdventRunner

class AdventDayNine(AdventRunner):
    def __init__(self):
        super().__init__()
        self.running_tally = []
        self.tally_position = 0
        self.match = []
        self.preamble = 25

    def processData(self, file_data):
        if self.additionalConfig['stage'] == 1:
            for index in range(0, len(file_data)):
                current = file_data[index]
                if current != '':
                    current = int(current)

                    if index > self.preamble:
                        if not self.testValue(current):
                            return current
                        else:
                            self.updateResults(current)
                    else:
                        self.running_tally.append(current)
        else :
            for index in range(0, len(file_data)):
                if file_data[index] != "":
                    total = 0
                    current_values = []
                    position = index
                    running = True
                    while running:
                        new_value = int(file_data[position])
                        current_values.append(new_value)
                        total += new_value

                        if total == self.additionalConfig['target']:
                            self.match.append(current_values)
                            current_values.sort()
                            self.outputDebug(current_values)
                            return current_values[0] + current_values[len(current_values)-1]
                        elif total > self.additionalConfig['target']:
                            current_values = []
                            total = 0
                            running = False
                        position += 1

                        if position > len(file_data):
                            running = False
            return self.match

    def updateResults(self, value):
        self.running_tally[self.tally_position] = value
        if self.tally_position == self.preamble:
            self.tally_position = 0
        else:
            self.tally_position += 1

    
    def testValue(self, value):
        for main_index in range(0, len(self.running_tally)):
            for inner_index in range(0, len(self.running_tally)):
                if inner_index == main_index:
                    continue
                total = self.running_tally[main_index] + self.running_tally[inner_index]
                if total == value:
                    return True
        return False

advent = AdventDayNine()
advent.addData("./data/day-9/input.txt")
advent.additionalConfig = {'verbose': False, 'stage':1}
total = advent.runScript()
print("Part 1: %i" %(total))

advent.additionalConfig = {'verbose': False, 'stage':2, 'target': total}
print("Part 2: %i" % (advent.runScript()))