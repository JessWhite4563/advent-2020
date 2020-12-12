import math
from generic import AdventRunner

class AdventDayTwelve(AdventRunner):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 0
        self.y = 0

        self.waypoint_x = 10
        self.waypoint_y = 1

    def processData(self, file_data):
        self.x = 0
        self.y = 0
        if self.additionalConfig['task'] == 1:
            return self.taskOne(file_data)
        else :
            return self.taskTwo(file_data)

    def taskTwo(self, file_data):
        for line in file_data:
            if line == '':
                continue
            opcode = line[:1]
            effect = int(line[1:])

            if opcode == 'F':
                self.applyWaypoint(effect)
            elif opcode == 'L' or opcode == 'R':
                self.rotateWaypoint(opcode, effect)
            else :
                self.slewWaypoint(opcode, effect)

        self.outputDebug((self.x, self.y))
        return abs(self.x) + abs(self.y)

    def slewWaypoint(self, heading, distance):
        if heading == 'N':
            self.waypoint_y += distance
        elif heading == 'E':
            self.waypoint_x += distance
        elif heading == 'S':
            self.waypoint_y -= distance
        elif heading == 'W':
            self.waypoint_x -= distance

    def rotateWaypoint(self, direction, degrees):
        if direction == 'L':
            angle = math.radians(degrees)
        else:
            angle = math.radians(360 - degrees)
        ox = 0
        oy = 0
        px = self.waypoint_x 
        py = self.waypoint_y

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        self.waypoint_x = round(qx)
        self.waypoint_y = round(qy)

    def applyWaypoint(self, count):
        for _ in range(0, count):
            self.x += self.waypoint_x
            self.y += self.waypoint_y

    def taskOne(self, file_data):
        current_dir = self.additionalConfig['initial_direction']
        
        for line in file_data:
            if line == '':
                continue

            opcode = line[:1]
            effect = int(line[1:])
            if opcode == 'F':
                heading = self.getHeading(current_dir)
                self.applyHeading(heading, effect)
            elif opcode == 'L':
                current_dir -= effect
                if current_dir < 0:
                    current_dir += 360
            elif opcode == 'R':
                current_dir += effect
                if current_dir > 359:
                    current_dir -= 360
            else :
                self.applyHeading(opcode, effect)

        self.outputDebug((self.x, self.y))
        return abs(self.x) + abs(self.y)

    def applyHeading(self, heading, distance):
        if heading == 'N':
            self.y += distance
        elif heading == 'E':
            self.x += distance
        elif heading == 'S':
            self.y -= distance
        elif heading == 'W':
            self.x -= distance

    def getHeading(self, current_dir):
        if current_dir == 0:
            return 'N'
        elif current_dir == 90:
            return 'E'
        elif current_dir == 180:
            return 'S'
        elif current_dir == 270:
            return 'W'


advent = AdventDayTwelve()
advent.addData("./data/day-12/input.txt")
advent.additionalConfig = {'verbose': False, 'initial_direction': 90, 'task':1}
print("Task One: %i" % (advent.runScript()))

advent.additionalConfig = {'verbose': False, 'initial_direction': 90, 'task':2}
print("Task Two: %i" % (advent.runScript()))