from generic import AdventRunner

class AdventDayEight(AdventRunner):
    def __init__(self):
        super().__init__()
        self.instruction_index = 0
        self.accumulator = 0
        self.instruction_history = []

    def resetData(self):
        super().resetData()
        self.instruction_index = 0
        self.accumulator = 0
        self.instruction_history = []

    def processData(self, file_data):
        next_step = True
        status = False
        while next_step :
            if self.instruction_index == len(file_data) - 1:
                status = True
                next_step = False
            elif self.instruction_index not in self.instruction_history :
                self.instruction_history.append(self.instruction_index)
                op = file_data[self.instruction_index]
                #self.outputDebug(op)
                self.processOp(op)
            else :
                next_step = False
        return status

    def processOp (self, op):
        task = op[:3]
        direction = op[4:5]
        num = int(op[5:])

        if task == 'acc' :
            if direction == '+' :
                self.accumulator += num
            else:
                self.accumulator -= num
        elif task == 'jmp' :
            self.outputDebug("%i - %s" % (num,op))
            if direction == '+' :
                self.instruction_index += num
            else :
                self.instruction_index -= num
        elif task == 'nop' :
            pass

        if task != 'jmp':
            self.instruction_index += 1

def update_line (op):
    task = op[:3]
    
    if task == 'jmp':
        op = op.replace(op[:3], 'nop')
    elif task == 'nop':
        op = op.replace(op[:3], 'jmp')
    else:
        return None
    return op

advent = AdventDayEight()
advent.addData("./data/day-8/input.txt")
advent.additionalConfig = {'verbose': False}

loop_run = True
data_index = 0
while loop_run :
    loop_op = True
    while loop_op:
        op = advent.imported_file[data_index]
        update_op = update_line(op)
        
        if update_op :
            loop_op = False
            advent.imported_file[data_index] = update_op

        data_index += 1

        if data_index == len(advent.imported_file):
            loop_op = False
            loop_run = False
            
    if not advent.runScript():
        advent.resetData()
    else :
        loop_run = False
        print(advent.accumulator)


