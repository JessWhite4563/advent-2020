from generic import AdventRunner
import math

def modinv(n, mod):
    return pow(n, mod-2, mod)

def chineseRemainderTheorem(mods, remainders):
    N = 1
    for m in mods:
        N *= m

    x = sum(r * N//m * modinv(N//m, m) for m, r in zip(mods, remainders))
    return x % N

class AdventDayThirteen(AdventRunner):

    def processData(self, file_data):
        if self.additionalConfig['task'] == 1:
            return self.taskOne(file_data)
        else:
            return self.taskTwo(file_data)

    def taskOne(self, file_data):
        lowest_time = None
        lowest_id = None
        
        timestamp = int(file_data[0])
        for id in file_data[1].split(','):
            if id != 'x':
                value = (math.floor(timestamp/ int(id) + 1 ) * int(id))
                if lowest_time is None or value < lowest_time:
                    lowest_time = value
                    lowest_id = int(id)
        return (lowest_time - timestamp) * lowest_id  
                
    def taskTwo(self, file_data):
        schedule = file_data[1].split(',')
        mods = []
        remainders = []
        for i, bus in enumerate(schedule):
            if bus == "x": 
                continue
            bus = int(bus)

            mod = bus
            remainder = (bus - i) % bus

            mods.append(mod)
            remainders.append(remainder)
        return chineseRemainderTheorem(mods, remainders)


advent = AdventDayThirteen()
advent.addData("./data/day-13/input.txt")
advent.additionalConfig = {'verbose': False, 'task': 1}
print("Task One: %i" % advent.runScript())

advent.additionalConfig = {'verbose': False, 'task': 2, 'start_point': 172}
print("Task Two: %i" % advent.runScript())