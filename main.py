import random
import tkinter

import numpy

import Brain
import mondo
import functions as f
import math

main = tkinter.Tk()


canvas = tkinter.Canvas(main, width=500, height=500, bg="#ebcdec")
canvas.pack()

w = mondo.World([500, 500], canvas,64,[{'x': 14, 'y': 14},  {'x': 4, 'y': 14}])



run=False
def input():
    global run
    run=not run
text=tkinter.Entry(main, textvariable=tkinter.StringVar(value="100"))
text.pack()
tkinter.Button(main,command=input,text="stop").pack()

lGenerazioni=tkinter.Label(main,text="0")
lGenerazioni.pack()

time=tkinter.Label(main,text="0")
time.pack()
round=tkinter.Label(main,text="1")
round.pack()
def loop():
    global run,text,lGenerazioni,time,round
    if(run):
        w.loop()
        round.config(text=w.round)
        time.config(text=w.t)
        if(w.loop()==0):
            print("rimasti")
            print(w.brains[0].name)
            print(w.brains[1].name)
            w.start(32,w.brains[0].Ms,w.brains[1].Ms)
            lGenerazioni.config(text =int(lGenerazioni.cget("text")) + 1)

            print("NUOVA GENERAZIONE")

    main.after(int(text.get()),loop)



loop()

main.mainloop()