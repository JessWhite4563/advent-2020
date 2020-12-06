from generic import AdventRunner

class AdventDaySix(AdventRunner):

    def processData(self, file_data):
        total_groups = []
        current_group = {}
        total_unique_answers = 0
        total_all_answers = 0

        group_counter = 0
        for row in file_data:
            if row == "":
                # new group reset
                total_groups.append(current_group)
                total_unique_answers += len(current_group.keys())

                for value in current_group.values():
                    if value == group_counter:
                        total_all_answers += 1

                current_group = {}
                group_counter = 0
            else:
                for answer in row:
                    try:
                        current_group[answer] += 1
                    except KeyError:
                        current_group[answer] = 1
                group_counter += 1
                    
        return 'Unique: %i, Everyone %i' % (total_unique_answers, total_all_answers)


advent = AdventDaySix()
advent.addData("./data/day-6/input.txt")
advent.additionalConfig = {'verbose': False}
print(advent.runScript())