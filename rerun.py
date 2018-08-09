#! /usr/bin/python3
from tkinter import *
import json
names=['Filename', 'Name', 'Té','Ké','Vé','Ép','Fp','Képzettségek','Ellenállások','Tulajdonságok']
dicta=[]
dicta1=[]
class Window:
	def __init__(self):
		self.app=Tk()
		self.app.title('Test Window')
	
	def runner(self):
		self.app.mainloop()

class Lab:
	def __init__(self,szoveg,row,col):
		Label(root.app, text=szoveg,bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=row, column=col)
class Ent:
	def __init__(self,row,col):
		self.entry=Entry(root.app)
		self.entry.grid(row=row,column=col+1)
		self.data=23

def maker():
	
	for i in range(len(names)):
		dicta.append(Lab(names[i],i,0))
		b.grid(row=1+i,column=0)
		b1.grid(row=1+i,column=1)
		dicta1.append(Ent(i,0))
root=Window()


def printer():
	for i in range(len(dicta1)):
		print (dicta1[i].entry.get())
b=Button(root.app,text='Maker',command=maker)
b.grid(row=0,column=0)
b1=Button(root.app, text='Printer',command=printer)
b1.grid(row=0,column=1)
root.runner()
