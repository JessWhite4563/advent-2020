class AdventRunner (object):
    def __init__(self):
        super().__init__()
        self.additionalConfig = {}
        self.imported_file = None

    def readFile(self, filename):
        f = open(filename, "r")
        result = f.read()
        return result

    def addData(self, filename):
        file_data = self.readFile(filename)
        processed = file_data.split("\n")
        self.imported_file = processed

    def runScript(self):
        return self.processData(self.imported_file)

    def outputDebug(self, output_data):
        if self.additionalConfig['verbose']:
            print(output_data)

    def processData(self,file_data):
        """ this is where the processing is done for the daily task """
