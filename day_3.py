from generic import AdventRunner
import copy

class AdventDayThree(AdventRunner):

    def processData(self, file_data):
        course_length = len(file_data) - 1
        course_width = len(file_data[0])
        tree_count = 0
        for index in range(0, course_length):
            modified_index = index * self.additionalConfig['down']
            if modified_index < course_length:
                total_x = index * self.additionalConfig['right']
                x = total_x % course_width

                if self.isTree([x, modified_index], file_data):
                    tree_count += 1

        self.OutputDebug("Total Trees :"+ str(tree_count))
        self.OutputDebug("Total Non Trees :"+ str(course_length - tree_count))
        return tree_count

    def isTree(self, position, file_data):
        row = file_data[position[1]]
        cell = row[position[0]]
        print_row = copy.copy(row)
        if cell == '#' :
            newstring = 'X'
        else:
            newstring = 'O'
        print_row = print_row[:position[0]] + newstring + print_row[position[0] + 1:]
        self.OutputDebug(print_row)
        return cell == '#'

configs = [
    {'down': 1, 'right': 1, 'verbose': False},
    {'down': 1, 'right': 3, 'verbose': False},
    {'down': 1, 'right': 5, 'verbose': False},
    {'down': 1, 'right': 7, 'verbose': False},
    {'down': 2, 'right': 1, 'verbose': False},
]

advent = AdventDayThree()
advent.addData("./data/day-3/input.txt")
total = 1
for config in configs:
    advent.additionalConfig = config
    total *= advent.runScript()

print(total)