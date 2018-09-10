#! /usr/bin/python3
import sys
import json
from tkinter import *
import pathlib
from functools import partial
import rerun

#some global variables that I had to exile from functions probably because I don't know a better solution
click_counter=0
newrow=0


#nest for the code which I only want to run if it's executed from an other program
def main():
	#another nonlocal lists used by the open_file function
	label_list=[]
	entry_list=[]
	
	#The Tkinter module which opens the root window
	class Window:
		def __init__(self):
			self.app=Tk()
			self.app.title('Reader')
			self.app.geometry("+0+0")
		def runner_func(self):
			self.app.mainloop()
	root=Window()
	
	#button command function which returns to the previous menu
	def backer():
		root.app.destroy()
		rerun.main()
	
	#button command function which displays the data of the chosen file
	def open_file(file_name):
		#take in the global variables
		global click_counter
		global newrow
		
		#count how many times the button got pressed
		click_counter+=1
		#print(file_name)
		#open the file displayed on the pressed button
		with open (str(file_name),'r') as f:
			data=json.load(f) 
		"""if the click counter reaches 5 it goes back to 1. Sheets continue on the next row. This keeps the sheets
		 inside the screen (my screen especially, 
		its not a cross platform solution)"""
		if click_counter==5:
			click_counter=1
			print ("Im full")
			newrow=newrow+len(data)
			print (newrow)

		#print (data)
		x=click_counter*2
		y=(click_counter*2)+1
		
		#print(click_counter,x,y)
		
		#print (root.app.winfo_reqwidth())
		#print (root.app.winfo_screenwidth())
		
			
			
				
		for i in range(len(data)):
			#backButt.b.grid(row=1+i,column=0)
			listButt.b.grid(row=1+i,column=0)
			label_list.append(Lab(root.app,rerun.names[i],newrow+i,x))
			entry_list.append(Ent(root.app,newrow+i,y,data[rerun.names[i]]))


	#button command function which lists every .json files in folder as clickable buttons
	def list_files():
		current=pathlib.Path('.')
		pattern="*.json"
		counter=0
		click_counter=0
		for f in current.glob(pattern):
			counter+=1
			string=str(f).replace('.json',"")
			commfunc=partial(open_file,f)
			Butt(counter,0,commfunc,string) 
	
	#Button class
	class Butt:
		def __init__(self,row,col,comm,text):
			self.b=Button(root.app,text=text,command=comm)
			self.b.grid(row=row,column=col)
	#Label class
	class Lab:
		def __init__(self,parent,text,row,col):
			self.l=Label(root.app,anchor=W,justify=LEFT, text=text,bg='IndianRed4', fg = 'black', font='none 12 bold')
			self.l.grid(row=row, column=col)
	#Entry class
	class Ent:
		def __init__(self,parent,row,col,ent):
			self.entry=Entry(root.app)
			self.entry.grid(row=row,column=col)
			self.entry.insert(0,ent)
	#Frame class (Not in use at the moment)
	class Fram:
		def __init__(self,row,col):
			self.frame=Frame(root.app)
			self.frame.grid(row=row,column=col)
	backButt =Butt(0,0,backer,"Back")
	listButt= Butt(0,1,list_files,"List")
	




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