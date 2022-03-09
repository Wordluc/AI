import random

import numpy as np
import random as rand
class Brain:

    def __init__(self):  # matrix=[{'x':x,'y':y},{'x':x,'y':y}...]
        self.Ms=[]
        self.nome=""

    def makeMatrix(self,matrix):
        for ind in matrix:
            M = []
            for i in range(ind['y']):
                M.append(self.makeArray(ind['x'], "rand"))
            self.Ms.append(np.matrix(M))
        return self.Ms

    def makeArray(self,n,v):

        if(v==""):
            return [0]*n
        array=[]
        for i in range(n):
            if(v=="rand"):
                x=100-random.random()*200
                array.append(x)
            else:
                array.append(v)
        return array
    def thinking(self,x,Ms):  # x=[input]
            x=np.transpose(x)

            for i in Ms:

                yi=np.dot(x,i)
                x=yi

            return yi

    def CombMatrix(self,a, b, struct):

        m = a.copy()
        rand = random.randint(1, m.shape[1] - 1)

        c=5
        for iC in range(m.shape[0]):
            for iR in range(m.shape[1]):

                if (iR < rand):
                    m[iC, iR] = b[iC, iR]


                if(random.randint(0,5)==1 and c!=0):
                    c-=1
                    r = 5 - random.random() * 10
                    m[iC, iR]+=r


        return m