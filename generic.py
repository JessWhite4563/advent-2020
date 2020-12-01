class AdventRunner (object):
    def __init__(self):
        self.additionalConfig = {}
        super()

    def readFile(self, filename):
        f = open(filename, "r")
        result = f.read()
        return result

    def runScript(self, filename):
        file_data = self.readFile(filename)
        processed = file_data.split("\n")
        self.processData(processed)

    def processData(self,file_data):
        """ this is where the processing is done for the daily task """