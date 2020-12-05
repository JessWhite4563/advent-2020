from generic import AdventRunner

class AdventDayFive(AdventRunner):

    def processData(self, file_data):
        highest_id = 0
        ids = []
        for row in file_data:
            if row != '':
                seat_id = self.getSeatId(row)
                ids.append(int(seat_id))
                if seat_id > highest_id:
                    highest_id = seat_id
        if self.additionalConfig['output'] == 'highest':
            return 'Highest: %i' % (int(highest_id))
        elif self.additionalConfig['output'] == 'seat':
            ids.sort()
            seat = -1
            for index in range(ids[0], ids[-1]):
                if index not in ids:
                    seat = index
            return 'Seat: %i' % (seat)

    def getSeatId(self, seatString):
        column = seatString[-3:]
        c_pos = self.binarySearch('L', 'R', self.additionalConfig['max_columns'], column)
        row = seatString[:-3]
        r_pos = self.binarySearch('F', 'B', self.additionalConfig['max_rows'], row)

        return r_pos * 8 + c_pos 
    
    def binarySearch(self, lower_mark, upper_mark, max, source):
        min_bounds = 0
        max_bounds = max
        difference = max_bounds - min_bounds

        for move in source:
            difference = difference / 2
            if move == lower_mark:
                if difference == 1:
                    return min_bounds
                max_bounds = max_bounds - difference
            elif move == upper_mark:
                if difference == 1:
                    return max_bounds - 1
                min_bounds = min_bounds + difference

configs = [
    {'verbose': False, 'max_rows': 128, 'max_columns': 8, 'output':'highest'},
    {'verbose': True, 'max_rows': 128, 'max_columns': 8, 'output':'seat'}
]
    
advent = AdventDayFive()
advent.addData("./data/day-5/input.txt")
for config in configs:
    advent.additionalConfig = config 
    print(advent.runScript())
