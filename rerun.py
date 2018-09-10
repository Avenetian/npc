#! /usr/bin/python3
	
from tkinter import *
import json
import Reader
names=['Filename', 'Name', 'Te','Ke','Ve','Ep','Fp','Kepzettsegek','Ellenallasok','Tulajdonsagok']

def main():
	dicta=[]
	dicta1=[]
	class Window:
		def __init__(self):
			self.app=Tk()
			self.app.title('Main Menu')
			self.app.configure(background='IndianRed4')
		def runner(self):
			self.app.mainloop()

	class Lab:
		def __init__(self,text,row,col):
			self.l=Label(root.app,anchor=W,justify=LEFT, text=text,bg='IndianRed4', fg = 'black', font='none 12 bold')
			self.l.grid(row=row, column=col)
	class Ent:
		def __init__(self,row,col):
			self.entry=Entry(root.app)
			self.entry.grid(row=row,column=col+1)
			self.data=23
	class Butt:
		def __init__(self,row,col,comm,text):
			self.b=Button(root.app,text=text,command=comm)
			self.b.grid(row=row,column=col)

	def maker():
		
		for i in range(len(names)):
			dicta.append(Lab(names[i],i,0))
			b.b.grid(row=1+i,column=0)
			b1.b.grid(row=1+i,column=1)
			b2.b.grid(row=1+i,column=2)
			dicta1.append(Ent(i,0))

	def new_frame():
		root.app.destroy()
		Reader.main()
	def printer():
		datapad={}
		for i in range(len(dicta1)):
			datapad[names[i]]=(dicta1[i].entry.get())

		print(datapad)
		with open(datapad['Filename']+'.json','w') as output:
			json.dump(datapad,output)
	
	root=Window()

	b=Butt(0,0,maker,'Maker')
	b1=Butt(0,1,printer,'Save')
	b2=Butt(0,2,new_frame,'Reader')


	root.runner()
if __name__ == '__main__':
	main()
