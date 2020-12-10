import copy

class AdventRunner (object):
    def __init__(self, input_is_numbers=False):
        super().__init__()
        self.additionalConfig = {}
        self.imported_file = None
        self.import_copy = None
        self.input_numbers = input_is_numbers

    def readFile(self, filename):
        try:
            f = open(filename, "r")
            result = f.read()
            return result
        except FileNotFoundError:
            print("WARNING - No File Found")
            return ''

    def addData(self, filename):
        file_data = self.readFile(filename)
        processed = file_data.split("\n")
        number_array = []
        if self.input_numbers:
            for line in processed:
                if line != '':
                    number_array.append(int(line))
            processed = number_array

        self.imported_file = processed
        self.import_copy = copy.copy(processed)

    def resetData(self):
        self.imported_file = copy.copy(self.import_copy)

    def runScript(self):
        return self.processData(self.imported_file)

    def outputDebug(self, output_data):
        if self.additionalConfig['verbose']:
            print(output_data)

    def processData(self,file_data):
        """ this is where the processing is done for the daily task """
