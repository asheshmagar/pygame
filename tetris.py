import tkinter as tk
import random
import pygame as pg


class Tetris:
    def __inti__(self,parent):
        self.parent=parent
        self.canvas=tk.Canvas(root,height=600,width=400)
        self.canvas.grid(row=0,column=0)
        self.tickrate=1000  
        self.parent.after(self.tickrate,self.tick)
    def tick(self):
        print('ticking')
        self.parent.after(self.tickrate,self.tick)
    def down(self):
        pass

    def left(self):
        



root=tk.Tk()
tetris = Tetris(root)
root.mainloop()
