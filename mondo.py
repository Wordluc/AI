import Brain
import character
import functions as f
import math



class World:
    canvas = object

    def declare(self):
        self.size = {'x': 0, 'y': 0}
        self.Cs = [object, object]
        self.struct=[]
        self.t=0
        self.Mt=30000
        self.best=[0,0]
        self.round=0
    def __init__(self, size, canvas,n,struct):
        super().__init__()
        self.declare()
        self.struct=struct.copy()

        f.arToDiz(self.size, size)
        self.canvas = canvas
        self.startN(n)
        self.ready()


    def get_position_ab(self, a, b):
        x = b.position['x'] - a.position['x']
        y = b.position['y'] - a.position['y']
        return {'x': x, 'y': y}

    def get_angle_ab(self, a, b):
        p = self.get_position_ab(a, b)
        return f.get_angle(p)

    def norm_angle(self,angle):
        if (angle > 180):
            angle = -360 + angle
        elif (angle < -180):
            angle = 360 + angle
        return angle
    def difAngle(self,a,b):
        if(a>=0 and b>=0):
            return b-a
        elif(a>=0 and b<=0):
            return b-a
        elif a<=0 and b>=0:
            return b-a
        elif a<=0 and b<=0:
            return b-a
        return 0
    def get_input(self,a,b):

        dn=self.get_position_ab(a,b)
        xn=dn['x']
        yn=dn['y']
        dn=math.sqrt(xn*xn+yn*yn)

        #angle=self.norm_angle(self.get_angle_ab(a,b))+self.norm_angle(a.angle)

        angle=self.difAngle(self.norm_angle(a.angle),self.norm_angle(self.get_angle_ab(a, b)))
        angle=self.norm_angle(angle)
        xi = a.position['x']-a.sizeMe['x']/2
        yi = a.position['y']-a.sizeMe['y']/2
        xf = self.size['x'] - xi
        yf = self.size['y'] - yi
        if(b.bull.status):
            p=self.get_position_ab(a,b.bull)
            xp=p['x']
            yp =p['y']
            es = 1
            dp = math.sqrt(xp * xp + yp * yp)

        else:
            xp = xn
            yp = yn
            dp = math.sqrt(xp * xp + yp * yp)

            es = 0

        anglep = self.difAngle(self.norm_angle(a.angle), self.norm_angle(f.get_angle({'x': xp, 'y': yp})))
        anglep = self.norm_angle(anglep)
        return [dn,xn,yn,angle,dp,xp,yp,es,anglep,yi,yf,xi,xf,a.bull.t]

    def startN(self,n):
        self.i=0
        self.brains=[]
        for i in range(n):
            self.brains.append(Brain.Brain())
            self.brains[i].makeMatrix(self.struct)
            self.brains[i].name=i
    def start(self,n,a,b):
        self.i = 0
        self.brains = []
        self.round=1
        for i in range(n):
            self.brains.append(Brain.Brain())
            self.brains[i].makeMatrix(self.struct)
            self.brains[i].name = i

            self.brains[i].Ms[0]=self.brains[i].CombMatrix(a[0],b[0],[self.struct[0]])
            self.brains[i].Ms[1] = self.brains[i].CombMatrix(a[1], b[1],[self.struct[1]])

    def ready(self):
        self.round+=1
        if(self.i==len(self.brains)):
            print("i=", self.i, "rimasti=", len(self.brains))
            self.i=0

        self.Cs[0] = character.Character([100, 200], [20, 20], self, self.canvas,self.struct)
        self.Cs[0].rotateN(180)
        self.Cs[1] = character.Character([300, 200], [20, 20], self, self.canvas,self.struct)
        self.Cs[0].brain = self.brains[self.i]
        self.Cs[1].brain = self.brains[self.i + 1]
        self.t = 0
        print("Stanno Combattento",self.Cs[0].brain.name,self.Cs[1].brain.name)


    def loop(self):

        self.canvas.delete('all')
        if (len(self.brains) == 2):
            print("finneee")
            self.t=0
            self.best = self.brains.copy()
            return 0  # fine
        r = [0, 0]
        self.t+=1
        if(self.t==self.Mt):
            self.t=0
            print("Riprova")
            if(self.best[0]!=0):
                self.brains[self.i].Ms[0]=self.brains[self.i].CombMatrix(self.best[0].Ms[0],self.best[1].Ms[0],self.struct[0])
                self.brains[self.i].Ms[1] =self.brains[self.i].CombMatrix(self.best[0].Ms[1], self.best[1].Ms[1],self.struct[1])
                self.brains[self.i+1].Ms[0] =self.brains[self.i+1].CombMatrix(self.best[0].Ms[0], self.best[1].Ms[0],self.struct[0])
                self.brains[self.i+1].Ms[1] = self.brains[self.i+1].CombMatrix(self.best[0].Ms[1], self.best[1].Ms[1],self.struct[1])
            else:
                self.brains[self.i].makeMatrix(self.struct)
                self.brains[self.i+1].makeMatrix(self.struct)
            self.Cs[0].brain = self.brains[self.i]
            self.Cs[1].brain = self.brains[self.i + 1]



        a=self.get_input(self.Cs[0], self.Cs[1])
        b=self.get_input(self.Cs[1], self.Cs[0])

        r[0]=self.Cs[0].loop(a, self.Cs[1].bull)

        r[1]=self.Cs[1].loop(b, self.Cs[0].bull)


        if r[0] == 1:

            print("Morto",self.Cs[0].brain.name)
            self.brains.pop(self.i)
            self.i += 1

            self.ready()

        elif r[1] == 1:

            print("Morto", self.Cs[1].brain.name)
            self.brains.pop(self.i+1)
            self.i += 1

            self.ready()




