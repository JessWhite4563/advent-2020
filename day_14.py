from generic import AdventRunner

class AdventDayFourteen(AdventRunner):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_array = {}

    def processData(self, file_data):
        self.data_array = {}
        if self.additionalConfig['task'] == 1:
            return self.taskOne(file_data)
        else:
            return self.taskTwo(file_data)

    def taskOne(self, file_data):
        current_mask = ''
        for line in file_data:
            if line == '':
                continue
            op, data = line.split(" = ")
            if op == "mask":
                current_mask = data
            if line[:3] == 'mem':
                output_position = op[4:-1]
                data = list(bin(int(data))[2:].zfill(36))
                for i, c in enumerate(current_mask):
                    if c != "X":
                        data[i] = c
                data = int("".join(data), 2)
                self.data_array[output_position] = data
        return sum(self.data_array.values())

    def taskTwo (self, file_data):
        mem = dict()
        mask = None

        for line in file_data:
            if line == '':
                continue
            var, data = line.split(" = ")
            if var == "mask":
                mask = data
            elif var.startswith("mem"):
                idx = var[4:-1]

                idx = list(bin(int(idx))[2:].zfill(36))
                for i, c in enumerate(mask):
                    if c == "1":
                        idx[i] = c

                floating = [i for i, c in enumerate(mask) if c == "X"]
                n = len(floating)
                for bits in range(2**n):
                    bits = bin(bits)[2:].zfill(n)

                    newIdx = idx[:]
                    for i, b in zip(floating, bits):
                        newIdx[i] = b

                    newIdx = int("".join(newIdx), 2)
                    mem[newIdx] = int(data)

        return sum(mem.values())

advent = AdventDayFourteen()
advent.addData("./data/day-14/input.txt")
advent.additionalConfig = {'verbose': False, 'task': 1}
print('task 1: %i' % advent.runScript())
advent.additionalConfig = {'verbose': False, 'task': 2}
print('task 2: %i' % advent.runScript())
