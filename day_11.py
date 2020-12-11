from generic import AdventRunner

class AdventDayEleven(AdventRunner):

    def initial_setup(self, file_data):
        dataset = []
        for index in range(0, len(file_data)):
            row = []
            for inner_index in range(0, len(file_data[index])):
                if file_data[index][inner_index] == 'L':
                     row.append(2)
                else:
                    row.append(0)
            dataset.append(row)
        return dataset

    def processData(self, file_data):
        dataset = self.initial_setup(file_data)
        running = True

        while running :
            new_dataset = []
            changes = 0
            for index in range(0, len(dataset)):
                new_row = []
                for inner_index in range(0, len(dataset[index])):
                    position = dataset[index][inner_index]

                    if position == 2:
                        count = self.getAdjacentSeats([index, inner_index], dataset)[0]
                        if count > 3:
                            new_row.append(1)
                            changes +=1
                        else:
                            new_row.append(2)

                    elif position == 1:
                        count = self.getAdjacentSeats([index, inner_index], dataset)[0]
                        if count == 0:
                            new_row.append(2)
                            changes +=1
                        else:
                            new_row.append(1)
                    else:
                        new_row.append(0)
                new_dataset.append(new_row)
            dataset = new_dataset

            if changes == 0 :
                running = False 
        return self.getAllOccupied(dataset)

    def getAllOccupied(self, dataset):
        occupied_count = 0
        for index in range(0, len(dataset)):
            self.outputDebug(dataset[index])
            for inner_index in range(0, len(dataset[index])):
                if dataset[index][inner_index] == 2:
                    occupied_count += 1
        return occupied_count

    def getAdjacentSeats(self, seatPosition, file_data):
        occupied_count = 0
        unoccupied_count = 0

        low_x = seatPosition[0] if seatPosition[0] - 1 < 0 else (seatPosition[0] -1)
        high_x = (seatPosition[0] + 1) if seatPosition[0] + 2 > len(file_data) else (seatPosition[0] +2)

        low_y = seatPosition[1] if seatPosition[1] - 1 < 0 else (seatPosition[1] -1)
        high_y = (seatPosition[1] + 1) if seatPosition[1] + 2 > len(file_data[seatPosition[1]]) else (seatPosition[1] +2)

        for index in range(low_x, high_x):
            for inner_index in range(low_y, high_y):
                if index == seatPosition[0] and inner_index == seatPosition[1]:
                    continue
                else:
                    if file_data[index][inner_index] == 2:
                        occupied_count += 1
                    elif file_data[index][inner_index] == 1:
                        unoccupied_count += 1
        return (occupied_count, unoccupied_count)

advent = AdventDayEleven()
advent.addData("./data/day-11/input.txt")
advent.additionalConfig = {'verbose': False}
print(advent.runScript())