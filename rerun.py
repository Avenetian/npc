#! /usr/bin/python3
	
from tkinter import *
import json
import Reader
def main():
	names=['Filename', 'Name', 'Te','Ke','Ve','Ep','Fp','Kepzettsegek','Ellenallasok','Tulajdonsagok']
	dicta=[]
	dicta1=[]
	class Window:
		def __init__(self):
			self.app=Tk()
			self.app.title('Test Window')
			self.app.configure(background='IndianRed4')
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
	class Fram:
		def __init__(self,wid,hei):
			self.frame=Frame(width=wid,height=hei,relief=SUNKEN)
			self.frame.grid(row=0,column=0)
	def maker():
		
		for i in range(len(names)):
			dicta.append(Lab(names[i],i,0))
			b.grid(row=1+i,column=0)
			b1.grid(row=1+i,column=1)
			dicta1.append(Ent(i,0))

	def new_frame():
		root.app.destroy()
		Reader.run_pls()
	def printer():
		datapad={}
		for i in range(len(dicta1)):
			datapad[names[i]]=(dicta1[i].entry.get())

		print(datapad)
		with open(datapad['Filename']+'.json','w') as output:
			json.dump(datapad,output)
	root=Window()


	b=Button(root.app,text='Maker',command=maker)
	b.grid(row=0,column=0)
	b1=Button(root.app, text='Printer',command=printer)
	b1.grid(row=0,column=1)
	b2=Button(root.app, text='Reader',command=new_frame)
	b2.grid(row=0,column=2)
	root.runner()
if __name__ == '__main__':
	main()
