import tkinter

import Object
import  functions as f
class Bull(Object.Object):
    def __init__(self,canvas):
        super().__init__()

        self.canvas=canvas
        self.status=False
        self.Mt = 100
        self.t=self.Mt

    def draw(self):

        if(self.status):
          x = self.position['x']
          y = self.position['y']
          self.canvas.create_oval(x,y,x+self.sizeMe['x'],y+self.sizeMe['y'])

    def fire(self,speed,position):

        if(not self.status and self.t==0):
            self.status=True
            x=position['x']-self.sizeMe['x']/2
            y = position['y']- self.sizeMe['y'] / 2
            f.arToDiz(self.speed, f.getArToDiz(speed))
            f.arToDiz(self.position, f.getArToDiz({'x':x,'y':y}))
            self.speed['x'] *= 10
            self.speed['y'] *= 10
            self.t=self.Mt

    def get_position(self):
        return [self.position['x']+self.sizeMe['x']/2,self.position['y']+self.sizeMe['y']/2]

    def loop(self,sizeM):
        if (self.t >0):
            self.t -= 1
        if(self.status):

           self.draw()



        if(self.status):
           x=self.position['x']+self.speed['x']
           y=self.position['y']+self.speed['y']
           if x >= self.sizeMe['y'] / 2 and x + self.sizeMe['x'] / 2 <= sizeM['x']:
               if y >= self.sizeMe['y'] / 2 and y + self.sizeMe['y'] / 2 <= sizeM['y']:
                   super().move([self.speed['x'], self.speed['y']])

                   return 0

           self.status=False
