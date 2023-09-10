from tkinter import * 
import pymysql

win5 = Tk () 
def Search  () :
	Sreg= Suid .get ()
	conobj = pymysql.connect (host ='localhost', user ='root', password ='', port = 3306) 
	curobj = conobj .cursor () 
	curobj .execute ('use MyClg;')
	d= f'select * from Info where userId  = "{Sreg}";'
	curobj .execute (d)
	data= curobj.fetchall ()
	print (data) 
	win5.destroy ()
	curobj.close () 
	conobj.close() 
	#import option   

win5.maxsize (800, 300 )
win5.minsize (800, 300 )
win5.title ("search Page")
win5.configure(bg='PaleGreen')
Label (win5, text = "Enter UserId to find details", font = ("Cooper", 18), bg = "#addbe6", fg="#000000",width=28, relief= "raised"). place (x= 50, y = 100)

Suid =Entry (win5,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
Suid. place (x= 500, y = 100 ) 

Button (win5, text = 'Search', font=("Elephant", 14), width=20,bg= "blue", fg="white",relief= "raised", activebackground="blue",command= Search).place (x= 300, y = 250)


win5.mainloop () 
 
