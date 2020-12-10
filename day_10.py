from generic import AdventRunner
import copy
import sys

sys.setrecursionlimit(20000)

class AdventDayTen(AdventRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.examples = []
        self.dead_ends = []
    def processData(self, file_data):
        if self.additionalConfig['task'] == 1:
            path = {1:[], 2:[], 3:[]}
            jolt_position = 0
            running = True
            jump = 1
            while(running):
                try:
                    file_data.index(jolt_position + jump)
                    
                    jolt_position += jump
                    path[jump].append(jolt_position)
                    jump = 1
                except ValueError:
                    jump += 1
                
                if jump == 4:
                    running = False
                    print(jolt_position)
                    path[3].append(jolt_position + 3)
                

            self.outputDebug(path)
            one_diff = len(path[1])
            three_diff = len(path[3])
            return one_diff * three_diff
        else:
            self.uniqueChainFinder([], 0, file_data)
            return len(self.examples)

    def uniqueChainFinder(self, current_list, jolt, file_data):
        if jolt == self.additionalConfig['target']:
            check = str(current_list)
            if check not in self.examples:
                self.examples.append(check)
        else:
            for index in range(1,4):
                new_pos = jolt + index
                try:
                    file_data.index(new_pos)
                    new_list = copy.copy(current_list)
                    new_list.append(new_pos)
                    self.uniqueChainFinder(new_list, new_pos, file_data)
                except ValueError:
                    self.dead_ends.append(new_pos)

                


advent = AdventDayTen(input_is_numbers=True)
advent.addData("./data/day-10/input.txt")
advent.additionalConfig = {'verbose': False, 'task':2, 'target': 176}
print(advent.runScript())