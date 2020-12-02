from generic import AdventRunner
import copy

class AdventDayTwo(AdventRunner):
    def __init__(self):
        super()
        self.results = []

    def processData(self, file_data):
        rule_one_count = 0
        rule_two_count = 0
        for row in file_data:
            split_res = row.split(':')
            if len(split_res) == 2:
                rule = self.processRule(split_res[0])

                if self.testRuleOne(rule, split_res[1].strip()) :
                    rule_one_count+= 1
                if self.testRuleTwo(rule, split_res[1].strip()) :
                    rule_two_count+= 1

        print("Rule One :" + str(rule_one_count))
        print("Rule Two :" + str(rule_two_count))

    def processRule(self, rule_string):
        rule_split = rule_string.split(' ')
        count_split = rule_split[0].split('-')

        rules = {'min': int(count_split[0]), 'max': int(count_split[1]), 'char': rule_split[1]}
        return rules

    def testRuleOne(self, rule_obj, password):
        count = password.count(rule_obj['char'])
        return count >= rule_obj['min'] and count <= rule_obj['max']

    def testRuleTwo(self, rule_obj, password):
        pos_1 = password[rule_obj['min']-1]
        pos_2 = password[rule_obj['max']-1]
    
        return (pos_1 == rule_obj['char']) != (pos_2 == rule_obj['char'])


advent = AdventDayTwo()
advent.runScript("./data/day-2/input.txt")
