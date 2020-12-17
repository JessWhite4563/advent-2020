from generic import AdventRunner

class AdventDaySixteen(AdventRunner):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rules = {}
        self.your_ticket = []
        self.other_tickets = []

    def processData(self, file_data):
        input_type = 1

        for line in file_data:
            if line == '':
                continue

            if line == 'your ticket:':
                input_type = 2
                continue
            elif line == 'nearby tickets:':
                input_type = 3
                continue

            if input_type == 1:
                self.processRule(line)
            elif input_type == 2:
                self.your_ticket = self.processTicket(line)
            elif input_type == 3:
                self.other_tickets.append(self.processTicket(line))

        if self.additionalConfig['task'] == 1:
            return self.taskOne()
        elif self.additionalConfig['task'] == 2:
            return self.taskTwo()

    def processRule(self, rule):
        name, rules = rule.split(': ')
        options = rules.split(' or ')
        ranges = []
        for option in options:
            low, high = option.split('-')
            ranges.append([int(low),int(high)])
        self.rules[name] = ranges
    
    def processTicket(self, ticket):
        return list(map(int, ticket.split(','))) 

    def testRules(self, field):
        for ranges in self.rules.values():
            if self.testRanges(ranges, field):
                return True
        return False

    def testRanges(self, ranges, field):
        for options in ranges:
            if field >= options[0] and field <= options[1]:
                return True
        return False

    def testRule(self, rule, field_index):
        ranges = self.rules[rule]
        for ticket in self.other_tickets:
            field = ticket[field_index]
            if not self.testRanges(ranges, field):
                return False
        return True


    
    def taskOne(self):
        total = 0
        for ticket in self.other_tickets:
            for field in ticket:
                if not self.testRules(field):
                    total += field
        return total

    def taskTwo(self):
        removeTickets = []
        for ticket in self.other_tickets:
            for field in ticket:
                if not self.testRules(field):
                    removeTickets.append(ticket)
                    break
        for ticket in removeTickets:
            self.other_tickets.remove(ticket)

        field_lookup = {}
        for rule in self.rules.keys():
            for index in range(0, len(self.your_ticket)):
                if self.testRule(rule, index):
                    if index in field_lookup.keys():
                        field_lookup[index].append(rule)
                    else:
                        field_lookup[index] = [rule]
        final = {}
        running = True
        while running:
            running = False
            for key, value in field_lookup.items():
                if len(value) == 1:
                  final[key] = value[0]
                  running = True
                  field_lookup = removeAssigned(field_lookup, value[0])
        total = 1
        for key, value in final.items():
            if 'departure' in value:
                total *= self.your_ticket[key]

        return total

def removeAssigned(field_lookup, field):
    for value in field_lookup.values():
        if field in value:
            value.remove(field)
    return field_lookup

advent = AdventDaySixteen()
advent.addData("./data/day-16/input.txt")
advent.additionalConfig = {'verbose': True, 'task': 2}
print(advent.runScript())

