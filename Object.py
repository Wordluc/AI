class Object:
    def declare(self):
        self.position = {'x': 0, 'y': 0}
        self.sizeMe = {'x': 10, 'y': 10}
        self.angle=0
        self.speed={'x':1,'y':1}
        self.speedangle=10
    def __init__(self):
        self.declare()
    def rotate(self,angle):
        self.angle+=angle
        if(self.angle>360 or self.angle<-360):
            self.angle=0
    def move(self, p):
        self.position['x'] += p[0]
        self.position['y'] += p[1]
