from generic import AdventRunner
import copy
import re

class AdventDayThree(AdventRunner):
    def __init__(self):
        super().__init__()
        self.eye_colour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def processData(self, file_data):
        passports = self.convertBatchToObjects(file_data)
        if self.additionalConfig['simple']:
            return 'simple :' + str(self.simpleTestPassports(passports))
        return 'advanced :' + str(self.advancedTestPassports(passports))

    def simpleTestPassports(self, passports):
        valid_passports = 0
        for passport in passports:
            keys = passport.keys()
            success = True
            for key in self.additionalConfig['required_keys']:
                if key not in keys:
                    success = False
                    break
            if success:
                valid_passports += 1
        return valid_passports

    def advancedTestPassports(self, passports):
        valid_passports = 0
        for passport in passports:
            success = True
            for key in self.additionalConfig['required_keys']:
                try:
                    value = passport[key]
                    if not self.validateInput(key, value):
                        success = False
                        break
                except KeyError:
                    success = False
            if success:
                valid_passports += 1
        return valid_passports

    def validateInput(self, key, value):
        if (key == 'byr'):
            return self.validateYear(value, 1920, 2002)
        elif (key == 'iyr'):
            return self.validateYear(value, 2010, 2020)
        elif (key == 'eyr'):
            return self.validateYear(value, 2020, 2030)
        elif (key == 'hgt'):
            return self.validateHGT(value)
        elif (key == 'hcl'):
            return self.validateHCL(value)
        elif (key == 'ecl'):
            return self.validateECL(value)
        elif (key == 'pid'):
            return self.validatePID(value)
        else:   
            return True

    def validateYear (self, value, earliest, latest):
        if len(value) != 4:
            return False
        if int(value) < earliest or int(value) > latest:
            return False
        return True

    def validateHGT (self, value):
        dimension = value[-2:]
        if dimension == 'cm':
            rules = {'max': 193, 'min': 150}
        elif dimension == 'in':
            rules = {'max': 76, 'min': 59}
        else:
            return False

        height = int(value[:-2])
        if height < rules['min'] or height > rules['max']:
            return False
        return True

    def validateHCL (self, value):
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)
        if not match:
            return False
        return True

    def validateECL (self, value):
        try:
            self.eye_colour.index(value)
        except ValueError:
            return False
        return True

    def validatePID (self, value):
        if len(value) != 9:
            return False
        return True

    def convertBatchToObjects(self, file_data):
        passports = []
        current_object = {}
        for row in file_data:
            if row == '':
                passports.append(current_object)
                current_object = {}
            else:
                fields = row.split(' ')
                for field in fields:
                    key_value = field.split(':')
                    current_object[key_value[0]] = key_value[1]
        return passports

configs = [
    {'simple': True, 'verbose': False, 'required_keys': ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']},
    {'simple': False, 'verbose': True, 'required_keys': ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']}
]

advent = AdventDayThree()
advent.addData("./data/day-4/input.txt")

for config in configs:
    advent.additionalConfig = config 
    print(advent.runScript())
