from tkinter import * 
import pymysql

win4 = Tk () 
def Del () :
	Dreg= Duid .get ()
	conobj = pymysql.connect (host ='localhost', user ='root', password ='', port = 3306) 
	curobj = conobj .cursor () 
	curobj .execute ('use MyClg;')
	d= f'delete from info where UserId = "{Dreg}";'
	curobj.execute (d)
	conobj.commit () 
	curobj.close () 
	conobj.close() 
	win4.destroy () 
	import option   

win4.maxsize (800, 300 )
win4.minsize (800, 300 )
win4.title ("Delete Page")
win4.configure(bg='PaleGreen')
Label (win4, text = "Enter UserId Which want to delete", font = ("Cooper", 18), bg = "#addbe6", fg="#000000",width=28, relief= "raised"). place (x= 50, y = 100)

Duid =Entry (win4,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
Duid. place (x= 500, y = 100 ) 

Button (win4, text = 'Delete', font=("Elephant", 14), width=20,bg= "blue", fg="white",relief= "raised", activebackground="blue",command= Del).place (x= 300, y = 250)


win4.mainloop () 
 
