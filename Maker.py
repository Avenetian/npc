#! /usr/bin/python3

print ('Hello World!')
import json
from tkinter import *
window = Tk()

#we have to make it in a class. Too hardcoded. pls


class MyLabel:
	
	def __init__(self,szoveg,row,col):
		self.szoveg=szoveg
		self.row=row
		self.col=col
		Label(window, text=szoveg,bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=row, column=col)
class MyEntry():
	def __init__(self,row,col):
		Entry(window).grid(row=row,column=col+1)
	def get(self):
		adat=Entry(window).get()
		print (adat)		
		
		

							


window.title('TestWindow')
window.configure(background = 'IndianRed4')
lab1=MyLabel('Filénamé',1,0)
ent1=MyEntry(1,0)
lab2=MyLabel('Név',2,0)
ent2=MyEntry(2,0)
def printer():
	ent1.get()
button=Button(window, text="Print",command=printer).grid(row=3,column=0)
window.mainloop()
"""Label(window, text='Filename', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=0, column=0)
Label(window, text='Név', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=1, column=0)
Label(window, text='Té', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=2, column=0)
Label(window, text='Ké', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=3, column=0)
Label(window, text='Vé', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=4, column=0)
Label(window, text='Ép', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=5, column=0)
Label(window, text='Fp', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=6, column=0)
Label(window, text='Sp', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=7, column=0)
Label(window, text='Képzettségek', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=8, column=0)
Label(window, text='Ellenállások', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=9, column=0)
Label(window, text='Tulajdonságok', bg='IndianRed4', fg = 'black', font='none 12 bold').grid(row=10, column=0)
e0=Entry(window)
e0.grid(row=0,column=1)
e1=Entry(window)
e1.grid(row=1,column=1)
e2=Entry(window)
e2.grid(row=2,column=1)
e3=Entry(window)
e3.grid(row=3,column=1)
e4=Entry(window)
e4.grid(row=4,column=1)
e5=Entry(window)
e5.grid(row=5,column=1)
e6=Entry(window)
e6.grid(row=6,column=1)

e7=Entry(window)
e7.grid(row=7,column=1)

e8=Entry(window)
e8.grid(row=8,column=1)

e9=Entry(window)
e9.grid(row=9,column=1)
e10=Entry(window)
e10.grid(row=10,column=1)"""
#this function goes to the above class too
"""def save():
	filename = e0.get()
	data1  = e1.get()
	data2 = e2.get()
	data3 = e3.get()
	data4 = e4.get()
	data5 = e5.get()
	data6 = e6.get()
	data7=e7.get()
	data8=e8.get()
	data9=e9.get()

	data10=e10.get()
	data = {'Nev':data1, 'Te': data2, 'Ke':data3, 'Ve':data4, 'Ep':data5, 'Fp':data6, 'Sp':data7, 'Kepz':data8, 'Ell':data9, 'Tul':data10}
	with open (filename + '.json' , 'w') as output:
		json.dump(data, output)

b = Button (window, text="Save", width=10, command=MyLabel.saver)
b.grid(row=3,column=0)"""
#window.mainloop()

