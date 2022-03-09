import math
import tkinter

import numpy as np

import Brain
import Bull
import functions as f
from PIL import Image,ImageTk

import Object

import Bull
class Character(Object.Object):
    world = object

    def __init__(self, position, sizeMe, world,canvas,struct):

        super().__init__()
        self.canvas=canvas
        self.bull=Bull.Bull(canvas)
        self.brain=Brain.Brain()

        image= Image.open(r"node.png")
        f.arToDiz(self.sizeMe, sizeMe)
        image=image.resize((self.sizeMe['x'], self.sizeMe['y']), Image.ANTIALIAS)
        self.sprite = ImageTk.PhotoImage(image)

        self.brain.makeMatrix(struct)
        f.arToDiz(self.position, position)

        self.world = world



    def rotateN(self,angle):
        self.rotate(angle)
        image = Image.open(r"node.png")

        image = image.rotate(-self.angle)
        image = image.resize((self.sizeMe['x'], self.sizeMe['y']), Image.ANTIALIAS)

        self.sprite = ImageTk.PhotoImage(image)

    def moveN(self, p):  # p={"x":,"y":}
        sizeMap = self.world.size
        x = self.position['x'] + p[0]
        y = self.position['y'] + p[1]

        if x > self.sizeMe['x']/2 and x + self.sizeMe['x']/2 < sizeMap['x']:
            if y > self.sizeMe['y']/2 and y + self.sizeMe['y']/2 < sizeMap['y']:
                super().move(p)

                return 0
        return 1

    def draw(self):
        xi = self.position['x']
        yi = self.position['y']
        self.canvas.create_image(xi,yi,image=self.sprite)

    def Mnorm(self,a):
        if a==0:
            return 0.0
        return a/math.sqrt(a*a)

    def checkFire(self,y):
        if (y >= 0):
            xp = math.cos(self.angle * math.pi / 180.0)
            yp = math.sin(self.angle * math.pi / 180.0)
            self.bull.fire({'x': xp, 'y': yp}, self.position.copy())

    def get_distance(self,bull):
        b=bull.get_position()
        return [self.position['x']-b[0],self.position['y']-b[1]]

    def loop(self,input,bullEnemy):


        y=self.brain.thinking(input,self.brain.Ms)

        y=np.transpose(y)
        p=[0,0]
        p[0]=self.Mnorm(y[1,0])*self.speed['x']
        p[1] =self.Mnorm(y[2,0])*self.speed['y']

        self.checkFire(y[0,0])
        if(y[3]!=0):
          a = y[3]/y[3]*5
          self.rotateN(int(a))

        d=self.get_distance(bullEnemy)

        d=math.sqrt(d[0]*d[0]+d[1]*d[1])
        die=False

        if(int(d)<=15):
            die=True



        self.draw()
        self.bull.loop(self.world.size)


        die=die or self.moveN(p)
        return die
