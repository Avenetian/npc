#! /usr/bin/python3
import sys
import json
from tkinter import *
import pathlib
from functools import partial
import rerun

def run_pls():
	class Lwindow:
		def __init__(self):
			self.app=Tk()
			self.app.title('Reader')
		def runner_func(self):
			self.app.mainloop()
	bye=Lwindow()
	def backer():
		bye.app.destroy()
		rerun.main()
	def open_file(file_name):
		print(file_name)
	def list_files():
		current=pathlib.Path('.')
		pattern="*.json"
		counter=0
		for f in current.glob(pattern):
			counter+=1
			string=str(f).replace('.json',"")
			commfunc=partial(open_file,f)
			Sheet(counter,0,string,commfunc) 
	class Butt:
		def __init__(self,row,col,comm,text):
			self.b=Button(bye.app,text=text,command=comm)
			self.b.grid(row=row,column=col)
	class Sheet:
		def __init__(self,row,col,text,comm):
			self.b=Button(bye.app, text=text,command=comm)
			self.b.grid(row=row,column=col)
	Butt(0,0,backer,"Back")
	Butt(0,1,list_files,"List")
	#valószínűleg ide egy decorator kell. Mondjuk még mindig nem tudom hogyan kéne Framere rakni egy buttont.
	#def out_runner():
	#	bye.runner_func()
	#	def runner():
	#		Butt(0,0,backer)
	#	runner()
		
"""readw = Tk()
serial = 0
readw.title('ReaderMenu')
Label(readw, text= "Read What?", bg='Gray40', fg = "white", font='none 12 bold').grid(row=0,column=0)
e0=Entry(readw)
e0.grid(row=0,column=1)
readw.configure(background = 'Gray40')
#ez az egész egy funkcióban van, elég ergya
def opener():
	#elcsiValue=int(e4.get())-4

	filename = e0.get()
	with open (filename + '.json','r') as f:
		data=json.load(f)
	
	opened = Tk()
	opened.title(filename+(str(serial)))
	opened.configure(background = 'Gray40')


	Label(opened, text="NÉV: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=0,column=0)
	e1=Entry(opened,bg='Gray50')
	e1.insert(0,data["Nev"])
	e1.grid(row=0,column=1)


	Label(opened, text="TÉ: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=1,column=0)
	e2=Entry(opened, bg='Gray50')
	e2.insert(0,data["Te"])
	e2.grid(row=1,column=1)


	Label(opened, text="KÉ: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=2,column=0)
	e3=Entry(opened,bg='Gray50')
	e3.insert(0,data["Ke"])
	e3.grid(row=2,column=1)

	Label(opened, text="VÉ: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=3,column=0)
	e4=Entry(opened,bg='Gray50')
	e4.insert(0,data["Ve"])
	e4.grid(row=3,column=1)

	Label(opened, text="ÉP: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=4,column=0)
	e5=Entry(opened,bg='Gray50')
	e5.insert(0,data["Ep"])
	e5.grid(row=4,column=1)


	Label(opened, text="FP: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=5,column=0)
	e6=Entry(opened,bg='Gray50')
	e6.insert(0,data["Fp"])
	e6.grid(row=5,column=1)

	Label(opened, text="SP: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=6,column=0)
	e7=Entry(opened,bg='Gray50')
	e7.insert(0,data["Sp"])
	e7.grid(row=6,column=1)

	Label(opened, text="Képzettségek: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=7,column=0)
	Label(opened, text=data["Kepz"],bg='Gray40', fg = 'white', font='none 12 bold').grid(row=7,column=1)
	
	Label(opened, text="Ellenállások: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=8,column=0)
	Label(opened, text=data["Ell"],bg='Gray40', fg = 'white', font='none 12 bold').grid(row=8,column=1)
	
	Label(opened, text="Tulajdonságok: ",bg='Gray40', fg = 'white', font='none 12 bold').grid(row=9,column=0)
	Label(opened, text=data["Tul"],bg='Gray40', fg = 'white', font='none 12 bold').grid(row=9,column=1)
	
	def elcsi():
		newVe=int(e4.get())
		newVe=newVe-4
		e4.delete(0,END)
		e4.insert(0,newVe)
		e4.configure(bg='red')

	def elcsiOff():
			pass


	b1 = Checkbutton(opened,text='Elcsigázott',bg='green', width=10, command=elcsi).grid(row=10,column=0)
	

	opened.mainloop()
def plusser():
	pass


def combine():
	global serial
	serial=serial+1
	opener()
def elcsi():
	newVe=int(e4.get())
	newVe=newVe-4
	e4.insert(0,newVe)
def exit():
	sys.exit(0)
b = Button (readw,text='Open', width=10, command=combine).grid(row=1,column=0)
b_quit = Button (readw, text='Quit All', width= 20, command=exit).grid(row=1,column=1)

"""