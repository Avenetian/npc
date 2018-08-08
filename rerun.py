#! /usr/bin/python3
from tkinter import *
import json
print ('Hello World')

class Window(object):
	def __init__(self):
		self.app=Tk()
		self.app.title('Test Window')
		
	def label(self,szoveg,row,col):
		self.szoveg=szoveg
		self.row=row
		self.col=col
		Label(self.app, text=szoveg,bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=row, column=col)
	def ent(self,row,col):
		self.entry=Entry(self.app)
		self.entry.grid(row=row,column=col+1)
		
		
	#def printer(self):
	#	self.data=self.entry.get()
	#	print (self.data)
		

	#def button(self,row,col):
	#	Button(self.app,text='Butt',command=self.printer).grid(row=row+1,column=col)
	
	def runner(self):
		self.app.mainloop()


	
root=Window()
root.label('Hello',0,0)
root.label('Darkness',1,0)
e1=root.ent(0,0)
e2=root.ent(1,0)

def printer():
	data=root.entry.get()
	print (data)
b=Button(root.app,text='Butt',command=printer)
b.grid(row=2,column=0)

root.runner()
