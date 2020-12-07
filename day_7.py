from generic import AdventRunner

class AdventDaySeven(AdventRunner):

    def __init__(self):
        super().__init__()
        self.processed = {}
        self.total = 0

    def processData(self, file_data):
        rules = self.processRules(file_data)
        count = self.findCount(rules, 'shiny gold bags')
        return count - 1

    def findCount(self, rules, current_container):
        if current_container in self.processed.keys():
            container_quantity = self.processed[current_container]
        else:
            container_dict = rules[current_container]
            if len(container_dict.items()) != 0:
                container_quantity = 1
                for key, value in container_dict.items():
                    if key in self.processed.keys():
                        content_num = self.processed[key]
                    else:
                        content_num = self.findCount(rules, key)
                    container_quantity += content_num * value
            else:
                container_quantity = 1
            
            self.processed[current_container] = container_quantity
        
        self.outputDebug(current_container + " " + str(container_quantity))
        return container_quantity

    def processRules(self, file_data):
        rules = {}
        for row in file_data:
            if (row != ''):
                row = row.replace('.', '')
                data = row.split(' contain ')
                contents = {}
                if data[1] != 'no other bags':
                    contents_string = data[1].split(', ')
                    for item in contents_string:
                        quantity_index = item.find(' ')
                        quantity = int(item[:quantity_index])
                        content = item[quantity_index + 1:]
                        if quantity == 1:
                            content = content + "s"
                        contents[content] = quantity
                rules[data[0]] = contents
        return rules

advent = AdventDaySeven()
advent.addData("./data/day-7/test2.txt")
advent.additionalConfig = {'verbose': False}
print(advent.runScript())